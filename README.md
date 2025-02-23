
# 🧑‍⚖️ LawLiot - AI Lawyer

Powerful RAG (Retrieval-Augmented Generation) system using Deepseek, LangChain, and Streamlit. This setup allows you to chat with PDFs and get accurate answers to complex questions about your local documents. IStarting with setting up Ollama’s Deepseek-r1 LLM model, which is known for its strong reasoning capabilities, integrate it with a LangChain-powered RAG pipeline and add a user-friendly Streamlit interface for real-time querying of your PDFs.  

## 🚀 Key Features

- **PDF Document Analysis**: Upload and process legal documents
- **Context-Aware Legal Q&A**: Get answers based on the uploaded document
- **RAG (Retrieval Augmented Generation) Pipeline**: Combines document retrieval with AI-generated responses
- **Vector Semantic Search**: Efficiently find relevant information in documents

## 🛠️ Technologies Used

- **Streamlit**: Web interface for user interaction
- **LangChain**: Framework for building the RAG pipeline
- **Groq**: High-performance LLM inference (DeepSeek R1 model)
- **Ollama**: Local embeddings generation
- **FAISS**: Vector database for efficient similarity search
- **PDFPlumber**: PDF text extraction
- **RecursiveCharacterTextSplitter**: Intelligent text chunking

## 📚 How It Works

1. **Document Processing**:
   - PDFs are uploaded and processed using PDFPlumber
   - Text is split into chunks using RecursiveCharacterTextSplitter
   - Chunks are embedded using Ollama (DeepSeek R1 model)
   - Embeddings are stored in a FAISS vector database

2. **Query Processing**:
   - User queries are processed through the RAG pipeline
   - Relevant document chunks are retrieved using FAISS
   - Groq LLM generates context-aware responses

3. **Response Generation**:
   - Custom prompt template ensures legally relevant answers
   - Responses are based strictly on the provided context

## 🚀 How to Use the Code

1. **Setup**:
   - Install required dependencies (Streamlit, LangChain, etc.)
   - Ensure Ollama is installed and running locally
   - Set up Groq API key as an environment variable

2. **Run the Application**:
   ```
   streamlit run frontend.py
   ```

3. **Usage**:
   - Upload a legal PDF document
   - Enter your legal query in the text area
   - Click "ASK LAWLIOT" to get AI-generated responses

## 📁 Project Structure

- `frontend.py`: Streamlit interface for user interaction
- `rag_pipeline.py`: Core RAG pipeline implementation
- `vector_database.py`: Document processing and vector database management

## ⚠️ Important Notes

- Ensure the Groq API key is securely stored and not exposed in the code
- The system relies on a local Ollama installation for embeddings
- Responses are generated based on the uploaded document's context

## 🔮 Future Enhancements

- Multi-document analysis
- Integration with legal databases
- Improved citation and source tracking
- Multi-language support

