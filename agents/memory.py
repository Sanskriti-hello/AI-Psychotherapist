import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

class MemoryStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.embeddings = SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2")
        self.collection = self.client.create_collection(name="cbt_memory", embedding_function=self.embeddings)

    def add_entry(self, id, text):
        self.collection.add(documents=[text], ids=[id])

    def query(self, query_text, n=3):
        results = self.collection.query(query_texts=[query_text], n_results=n)
        return results['documents'][0] if results['documents'] else []
