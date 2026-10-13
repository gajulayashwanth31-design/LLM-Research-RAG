from vector_store import get_vector_store
from embeddings import get_embedding_model

def get_retriever():

    embedding_model = get_embedding_model()

    vector_store = get_vector_store(
        embedding_model
    )

    return vector_store
def retrieve_documents(vector_store,query, k=5):

    #embedding_model = get_embedding_model()
    #vector_store = get_vector_store(embedding_model)

    results = vector_store.similarity_search(query, k=k)

    return results