from langchain_chroma import Chroma


COLLECTION_NAME = "llm_knowledge_base"
PERSIST_DIRECTORY = "./chroma_db"


def get_vector_store(embedding_model):
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        persist_directory=PERSIST_DIRECTORY
    )


def add_documents(vector_store, chunks):
    vector_store.add_documents(chunks)
    print(f"Added {len(chunks)} chunks to ChromaDB")