import os

class Config:
    """
    Configuration class to set up environment variables for the document searcher.
    - TOKENIZERS_PARALLELISM: Manages parallel tokenization
    - MODEL_NAME: The name of the model used for embeddings.
    - CSV_FILE_PATH: Path to the CSV file containing the documents to be indexed.
    - CHUNK_SIZE: Size of the text chunks to split documents into.
    - CHUNK_OVERLAP: The number of characters to overlap between chunks.
    - PERSIST_DIRECTORY: Directory where the processed vector database will be stored.
    """
    TOKENIZERS_PARALLELISM = os.getenv("TOKENIZERS_PARALLELISM", "false")
    MODEL_NAME = os.getenv("MODEL_NAME", "dangvantuan/sentence-camembert-large")
    CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "llm_data_augmentation/RAG/medicines_management/data/csv/clean_medicaments.csv")
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1800))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))
    PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY", "llm_data_augmentation/RAG/medicines_management/data/chroma_db")
