from langchain_chroma import Chroma

class VextorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name = None,
        )
        self.splite = None;