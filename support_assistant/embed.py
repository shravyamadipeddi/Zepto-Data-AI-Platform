from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load all text files
loader = DirectoryLoader(
    "support_assistant/docs",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

print(f"Created {len(docs)} chunks")

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create Chroma vector database
db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="support_assistant/chroma_db"
)

db.persist()

print("Vector database created successfully!")