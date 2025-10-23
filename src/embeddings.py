import os
import fitz
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def create_vectorstore(pdf_path, persist_dir="./chroma_db"):
    pdf_text = extract_text_from_pdf(pdf_path)
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(pdf_text)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    os.makedirs(persist_dir, exist_ok=True)

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        collection_name="finance_pdf_docs",
        persist_directory=persist_dir
    )
    # Persist is automatic in newer versions when persist_directory is specified
    return vectorstore
