---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Applications"
keywords:
  - GPT-3
  - Few-Shot Learning
  - Natural Language Processing
  - Text Generation
  - Question Answering
  - Translation
generated_from: "Original Research Paper"
---

# Question Answering

## Closed-Book Question Answering

GPT-3 can answer broad factual questions without retrieving external documents.

The paper evaluates Natural Questions, WebQuestions, and TriviaQA.

The model improves substantially from zero-shot to few-shot settings.

# Translation

## Multilingual Translation

GPT-3 demonstrates translation capability despite being trained primarily on English text.

The paper evaluates English-French, French-English, English-German, German-English, English-Romanian, and Romanian-English translation.

## Few-Shot Translation

Providing demonstrations improves translation performance.

The paper observes stronger performance when translating into English than when translating from English.

# Text Completion

## Sentence and Paragraph Completion

GPT-3 can complete partial text based on the preceding context.

The paper evaluates tasks including LAMBADA, StoryCloze, and HellaSwag.

# Language Modeling

## Next-Token Prediction

GPT-3 can be evaluated directly as a language model using perplexity.

The paper reports a zero-shot perplexity of 20.5 on the Penn Tree Bank dataset.

# Commonsense Reasoning

## Physical and Scientific Reasoning

GPT-3 is evaluated on PIQA, ARC, and OpenBookQA.

These tasks test knowledge and reasoning about physical and scientific situations.

# Natural Language Inference

## Textual Reasoning

GPT-3 can be applied to inference-style tasks through natural-language task formatting.

However, the paper identifies NLI as one of the areas where GPT-3 remains relatively weak.

# Word Manipulation

## Unscrambling

GPT-3 is evaluated on synthetic tasks involving word manipulation.

Demonstrations allow the model to infer the transformation required by the task.

# Arithmetic

## Few-Shot Arithmetic

The paper evaluates GPT-3 on arithmetic tasks.

The experiments test whether the model can perform arithmetic behavior based on examples supplied in the context.

# Novel Word Usage

## Task Adaptation

GPT-3 is evaluated on tasks where a new word is defined and the model must use the word appropriately.

This probes whether the model can rapidly adapt to information introduced in context.

# Text Generation

## News Article Generation

GPT-3 can generate news-style articles.

Human evaluators sometimes have difficulty distinguishing GPT-3-generated articles from human-written articles.

# Writing Assistance

## Potential Application

The paper identifies writing assistance as a possible beneficial application of increasingly capable language models.

# Code Completion

## Potential Application

The paper identifies code and writing auto-completion as possible beneficial applications.

# Grammar Assistance

## Potential Application

Large language models can potentially assist with grammar correction and related writing tasks.

# Search Assistance

## Potential Application

The paper discusses improving search-engine responses as a possible application of language models.

# Game Narrative Generation

## Potential Application

Language models can be used for generating narrative content in games.

# Question Answering Systems

## General Interface

The ability to represent different tasks as text allows one language model to act as a general-purpose language interface.

The paper demonstrates this through question answering, translation, classification-style tasks, reasoning tasks, and text generation.