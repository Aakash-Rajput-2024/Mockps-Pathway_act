
import os
import sys
from pathlib import Path
from embeddings import create_vectorstore

def find_pdf_files(directory="."):
    """Find all PDF files in the given directory and subdirectories."""
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def initialize_database():
    """Initialize the vector database with PDF documents."""
    print("=== Finance Bot Database Initialization ===")
    print("Looking for PDF documents...")
    
    # Find PDF files
    pdf_files = find_pdf_files()
    
    if not pdf_files:
        print("\nNo PDF files found!")
        print("\nTo add PDF documents:")
        print("1. Place your financial PDF files in the project directory")
        print("2. Run this script again")
        print("\nExample PDF files you might want to add:")
        print("- Investment guides")
        print("- Financial planning documents") 
        print("- Market analysis reports")
        print("- Retirement planning materials")
        return False
    
    print(f"\nFound {len(pdf_files)} PDF file(s):")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"  {i}. {pdf_file}")
    
    print("\nProcessing PDFs and creating vector database...")
    
    try:
        # Process the first PDF (you can modify this to process multiple PDFs)
        pdf_path = pdf_files[0]
        print(f"Processing: {pdf_path}")
        
        vectorstore = create_vectorstore(pdf_path, persist_dir="./chroma_db")
        print("Vector database created successfully!")
        print(f" Database location: ./chroma_db")
        
        return True
        
    except Exception as e:
        print(f" Error creating vector database: {e}")
        return False

if __name__ == "__main__":
    success = initialize_database()
    
    if success:
        print("\n Database initialization complete!")
        print("You can now run the chatbot with: python src/demo.py")
    else:
        print("\nDatabase initialization failed or no PDFs found.")
        print("The chatbot will still work using web search as fallback.")
