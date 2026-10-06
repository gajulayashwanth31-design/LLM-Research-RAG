from langchain_huggingface import HuggingFaceEmbeddings


EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )