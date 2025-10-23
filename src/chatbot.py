from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from ollama import chat
from prompts import system_p
from web_utils import web_search

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma(persist_directory="./chroma_db", collection_name="finance_pdf_docs", embedding_function=embedding_model)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

def llama3_qa(user_query, system_prompt=system_p):
    context_docs = retriever.invoke(user_query)
    context_text = "\n\n".join([doc.page_content for doc in context_docs])

    if len(context_text) < 200:
        web_results = web_search(user_query)
        context_text += "\n\nWeb Results:\n" + "\n".join(web_results)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion:\n{user_query}"}
    ]

    response = chat(model="llama3", messages=messages)
    return response['message']['content']
