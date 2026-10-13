import re
import string
from collections.abc import Mapping, Sequence
from typing import Any


_CASUAL_RESPONSES = {
    "hi": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "hello": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "hey": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "hi there": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "hello there": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "hey there": "Hi! 👋 I'm your LLM research assistant. Ask me anything about the LLM research papers in my knowledge base.",
    "good morning": "Good morning! What would you like to explore in the LLM research papers?",
    "good afternoon": "Good afternoon! What would you like to explore in the LLM research papers?",
    "good evening": "Good evening! What would you like to explore in the LLM research papers?",
    "how are you": "I'm doing well, thanks! What would you like to explore in the LLM research papers?",
    "how are you doing": "I'm doing well, thanks! What would you like to explore in the LLM research papers?",
    "what's up": "Hi! What would you like to explore in the LLM research papers?",
    "thanks": "You're welcome! Feel free to ask another question.",
    "thanks a lot": "You're welcome! Feel free to ask another question.",
    "thank you": "You're welcome! Feel free to ask another question.",
    "thanks so much": "You're welcome! Feel free to ask another question.",
    "thank you so much": "You're welcome! Feel free to ask another question.",
    "bye": "Goodbye! 👋",
    "goodbye": "Goodbye! 👋",
}

_FOLLOW_UP_ONLY = {
    "elaborate",
    "explain further",
    "why",
    "how",
    "give me an example",
    "give an example",
    "what does that mean",
}

_QUESTION_PREFIX = re.compile(
    r"^(?:what|who|which)\s+(?:is|are|was|were)\s+"
    r"|^(?:explain|describe|define|summari[sz]e)\s+"
    r"|^tell me about\s+"
    r"|^give me an overview of\s+",
    re.IGNORECASE,
)
_COMPARISON = re.compile(
    r"(?:differences?|comparison)\s+between\s+(.+?)\s+and\s+(.+?)(?:[?.!,]|$)",
    re.IGNORECASE,
)
_FOLLOW_UP_CUE = re.compile(
    r"\b(?:it|this|that|they|them|these|those|its|their|the above|"
    r"the previous concept)\b",
    re.IGNORECASE,
)


def casual_response(message: str) -> str | None:
    """Return a deterministic reply only for a standalone casual message."""
    normalized = " ".join(
        message.strip().lower().strip(string.punctuation).split()
    )
    return _CASUAL_RESPONSES.get(normalized)


def _clean_topic(topic: str) -> str:
    topic = re.sub(r"\s+", " ", topic.strip(" \t\n\r.,!?;:"))
    topic = re.sub(r"^(?:the|a|an)\s+", "", topic, flags=re.IGNORECASE)
    topic = re.sub(
        r"\s+(?:again|further|in more detail)$",
        "",
        topic,
        flags=re.IGNORECASE,
    )
    topic = re.sub(
        r"\s+(?:and explain|and describe|and discuss)\s+.*$",
        "",
        topic,
        flags=re.IGNORECASE,
    )
    return topic


def _topics_from_question(question: str) -> list[str]:
    comparison = _COMPARISON.search(question.strip())
    if comparison:
        left = _clean_topic(comparison.group(1))
        right = _clean_topic(comparison.group(2))
        if left and right:
            return [left, right]

    topic = _QUESTION_PREFIX.sub("", question.strip(), count=1)
    topic = re.sub(r"[?.!,;:]+$", "", topic).strip()
    topic = re.sub(
        r"^(?:the\s+)?(.+?)\s+part\s+in\s+more\s+detail$",
        r"\1",
        topic,
        flags=re.IGNORECASE,
    )
    topic = re.sub(r"^(?:the|a|an)\s+", "", topic, flags=re.IGNORECASE)
    topic = _clean_topic(topic)
    return [topic] if topic else []


def _recent_topics(history: Sequence[Mapping[str, Any]]) -> list[str]:
    recent_messages = history[-8:]
    topics: list[str] = []
    for message in reversed(recent_messages):
        if message.get("role") == "assistant":
            retrieval_query = message.get("retrieval_query")
            if isinstance(retrieval_query, str):
                topics.extend(_topics_from_question(retrieval_query))
        elif message.get("role") == "user":
            content = message.get("content")
            if isinstance(content, str):
                topics.extend(_topics_from_question(content))

    unique_topics: list[str] = []
    seen: set[str] = set()
    for topic in topics:
        normalized = topic.casefold()
        if normalized not in seen:
            seen.add(normalized)
            unique_topics.append(topic)
    return unique_topics


def _choose_topic(
    message: str,
    topics: Sequence[str],
) -> str | None:
    lowered_message = message.casefold()
    for topic in topics:
        if topic.casefold() in lowered_message:
            return topic
    return topics[0] if topics else None


def _is_follow_up(message: str) -> bool:
    normalized = message.casefold().strip(string.punctuation + " ")
    return (
        normalized in _FOLLOW_UP_ONLY
        or bool(_FOLLOW_UP_CUE.search(message))
        or bool(
            re.search(
                r"\bpart\b.*\b(?:again|further|detail)\b",
                normalized,
            )
        )
        or bool(
            re.match(
                r"^(?:can you |could you |please )?"
                r"(?:elaborate|expand on|say that again)\b",
                normalized,
            )
        )
    )


def resolve_follow_up_query(
    message: str,
    history: Sequence[Mapping[str, Any]],
) -> str:
    """Resolve a referential follow-up into a standalone retrieval query."""
    query = message.strip()
    if not _is_follow_up(query):
        return query

    topics = _recent_topics(history)
    topic = _choose_topic(query, topics)
    if not topic:
        return query

    normalized = query.casefold().strip(string.punctuation + " ")
    if normalized in {"why", "how"}:
        return f"Why is {topic} important?" if normalized == "why" else (
            f"How does {topic} work?"
        )
    if normalized in {"elaborate", "explain further"}:
        return f"Explain {topic} in more detail."
    if normalized in {"give me an example", "give an example"}:
        return f"Give me an example of {topic}."
    if normalized == "what does that mean":
        return f"What does {topic} mean?"

    explicit_topic = next(
        (
            candidate
            for candidate in topics
            if candidate.casefold() in query.casefold()
        ),
        None,
    )
    if explicit_topic:
        query = re.sub(
            r"\bthe\s+"
            + re.escape(explicit_topic)
            + r"\s+part\b",
            explicit_topic,
            query,
            flags=re.IGNORECASE,
        )
        return query

    if re.search(r"\bits\b", query, flags=re.IGNORECASE):
        query = re.sub(
            r"\bits\b",
            f"{topic}'s",
            query,
            flags=re.IGNORECASE,
        )
    else:
        query = re.sub(
            r"\b(?:it|this|that|they|them|these|those|the above|"
            r"the previous concept)\b",
            topic,
            query,
            flags=re.IGNORECASE,
        )
    return query
