import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from retrieval import retrieve_documents


load_dotenv()


MODEL = "gemini-3.1-flash-lite"


llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0
)


SYSTEM_PROMPT = """
You are an educational assistant specialized in Large Language Models.

Answer the user's question using only the provided context.

Rules:
- Do not use outside knowledge.
- If the context does not contain enough information, say:
  "I don't have enough information in the provided knowledge base."
- Explain concepts clearly and at a student-friendly level.

Context:
{context}
"""


def answer_question(question):

    # 1. Retrieve relevant chunks
    docs = retrieve_documents(question, k=3)

    # 2. Combine chunks into context
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # 3. Insert context into the prompt
    system_prompt = SYSTEM_PROMPT.format(
        context=context
    )

    # 4. Send context + question to Gemini
    response = llm.invoke([
        ("system", system_prompt),
        ("human", question)
    ])

    # 5. Return generated text
    return response.content