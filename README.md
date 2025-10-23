# Finance Chatbot

An intelligent financial assistant powered by AI that provides personalized financial advice using advanced language models and retrieval-augmented generation (RAG) capabilities.

## Features

- **Interactive Chat Interface**: Real-time conversation with a financial AI assistant
- **Document Processing**: Processes financial PDFs to build a knowledge base
- **Web Search Integration**: Falls back to web search when local knowledge is insufficient
- **Data Extraction**: Automatically extracts and summarizes user financial information
- **Vector Database**: Uses ChromaDB for semantic search over financial documents
- **Local LLM**: Runs entirely offline using Ollama with Llama3 model

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed with Llama3 model
- Internet connection (for web search fallback)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Aakash-Rajput-2024/finance-chatbot.git
cd finance-chatbot
```

2. Run the setup script:
```bash
chmod +x run_src.sh
./run_src.sh
```

The script will automatically:
- Create a virtual environment
- Install all required dependencies
- Set up the project structure

### Usage

After running the setup script, choose from the following options:

1. **Interactive Chat**: Start a conversation with the financial assistant
2. **Test Mode**: Run predefined test scenarios
3. **Initialize Database**: Process PDF documents to build knowledge base
4. **Exit**: Close the application

## Project Structure

```
finance-chatbot/
├── src/
│   ├── chatbot.py          # Main chatbot logic
│   ├── data_extractor.py    # User data extraction
│   ├── demo.py             # Interactive chat interface
│   ├── dummy_test.py       # Test with predefined prompts
│   ├── embeddings.py       # PDF processing and vectorization
│   ├── init_database.py    # Database initialization
│   ├── prompts.py         # System prompts
│   └── web_utils.py       # Web search functionality
├── requirements.txt        # Python dependencies
├── run_src.sh            # Setup and run script
└── README.md             # This file
```

## How It Works

The chatbot uses a multi-layered approach to provide accurate financial advice:

1. **Local Knowledge Base**: Processes financial PDFs and creates vector embeddings
2. **Semantic Search**: Retrieves relevant information from the knowledge base
3. **Web Search Fallback**: Uses web search when local knowledge is insufficient
4. **LLM Processing**: Generates responses using the Llama3 model via Ollama
5. **Data Extraction**: Automatically extracts user financial information for personalization

## Dependencies

- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for embeddings
- **Ollama**: Local LLM server
- **PyMuPDF**: PDF document processing
- **Sentence Transformers**: Text embeddings
- **Google Search**: Web search integration


