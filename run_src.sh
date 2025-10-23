#!/bin/bash

echo "=== Finance Bot Setup (src-only) ==="
echo ""

if [ ! -d "src" ]; then
    echo "Error: 'src' directory not found!"
    echo "Please run this script from the project root directory."
    echo "Make sure the 'src' folder is present."
    exit 1
fi

echo "Found src directory"
echo ""

if [ ! -d "venv" ] && [ ! -d "env" ] && [ ! -d ".venv" ]; then
    echo "No virtual environment found!"
    echo "Creating a new virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created!"
fi

if [ -d "venv" ]; then
    echo "Activating virtual environment (venv)..."
    source venv/bin/activate
elif [ -d "env" ]; then
    echo "Activating virtual environment (env)..."
    source env/bin/activate
elif [ -d ".venv" ]; then
    echo "Activating virtual environment (.venv)..."
    source .venv/bin/activate
else
    echo "Could not find or create virtual environment"
    exit 1
fi

echo "Virtual environment activated!"
echo ""

if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found!"
    echo "Creating requirements.txt with necessary dependencies..."
    cat > requirements.txt << 'EOF'
langchain>=1.0.0
langchain-community>=0.4.0
langchain-core>=1.0.0
langchain-huggingface>=1.0.0
langchain-chroma>=1.0.0
sentence-transformers>=2.2.2
huggingface-hub>=0.35.0
transformers>=4.30.0
chromadb>=1.2.0
ollama>=0.0.17
PyMuPDF>=1.22.5
googlesearch-python>=1.1.0
numpy>=1.26.0
tqdm>=4.66.1
requests>=2.32.0
pydantic>=2.0.0
EOF
    echo "requirements.txt created!"
fi

echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed!"
echo ""

if ! command -v ollama &> /dev/null; then
    echo "Ollama not found!"
    echo "Please install Ollama first:"
    echo "1. Visit: https://ollama.ai"
    echo "2. Download and install Ollama"
    echo "3. Run: ollama pull llama3"
    echo ""
    echo "Continuing without Ollama check..."
fi

echo "Choose an option:"
echo "1. Interactive Chat (demo.py)"
echo "2. Test with predefined prompts (dummy_test.py)"
echo "3. Initialize Database with PDFs"
echo "4. Exit"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "Starting interactive chat..."
        echo "Type 'exit' to quit the chat."
        echo ""
        cd src
        python demo.py
        ;;
    2)
        echo "Running test with predefined prompts..."
        cd src
        python dummy_test.py
        ;;
    3)
        echo "Initializing database with PDF documents..."
        cd src
        python init_database.py
        ;;
    4)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac