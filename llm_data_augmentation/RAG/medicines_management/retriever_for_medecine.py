import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .config import Config

os.environ["TOKENIZERS_PARALLELISM"] = Config.TOKENIZERS_PARALLELISM

class DocumentSearcher:
    """
    A class to initialize and utilize a vector database for document searching.
    Utilizes custom embeddings from HuggingFace specifically tailored for French language queries.
    """
    def __init__(self):
        self.vector_db = self._initialize_components()

    def _initialize_components(self):
        embedding_function = HuggingFaceEmbeddings(model_name=Config.MODEL_NAME, model_kwargs={'device': 'cpu'})
        loader = CSVLoader(file_path=Config.CSV_FILE_PATH, csv_args={"delimiter": ",", "quotechar": '"', "fieldnames": ['medicament_info']})
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP)
        docs = text_splitter.split_documents(documents)
        vector_db = Chroma.from_documents(docs, embedding_function, persist_directory=Config.PERSIST_DIRECTORY)
        return vector_db

    def search_db(self, prompt):
        print(f"Searching for: {prompt}")
        search_results = self.vector_db.similarity_search(prompt, k=1)
        return search_results

if __name__ == "__main__":
    document_searcher = DocumentSearcher()
    prompt = "Céfalexine"
    results = document_searcher.search_db(prompt)
    print(results)
