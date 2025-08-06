# MedSync AI Chatbot - Streamlit Version

A modern, interactive medical chatbot built with Streamlit that provides intelligent responses to medical queries using AI and vector search.

## 🚀 Features

- **Modern UI**: Clean, responsive interface built with Streamlit
- **AI-Powered**: Uses Google's Gemini AI for intelligent responses
- **Vector Search**: Leverages Pinecone for semantic search across medical documents
- **Real-time Chat**: Interactive chat interface with message history
- **Medical Knowledge**: Trained on medical documents and literature
- **Error Handling**: Robust error handling and user feedback

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Sadiya-125/MedSync-AI-Chatbot.git
   cd MedSync-AI-Chatbot
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory with:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

## 🚀 Running the Application

### Option 1: Direct Streamlit Run

```bash
streamlit run streamlit_app.py
```

### Option 2: With Custom Port

```bash
streamlit run streamlit_app.py --server.port 8501
```

### Option 3: With Custom Host

```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```

## 📋 Prerequisites

- **Python 3.8+**
- **Pinecone Account**: For vector database
- **Google AI Studio Account**: For Gemini API access
- **Medical Documents**: PDF files in the `data/` directory (for initial setup)

## 🔧 Configuration

### Environment Variables

- `PINECONE_API_KEY`: Your Pinecone API key
- `GEMINI_API_KEY`: Your Google Gemini API key

### Pinecone Setup

1. Create a Pinecone account at [pinecone.io](https://pinecone.io)
2. Create a new index named "medical-chatbot"
3. Set the dimension to 384 (for the sentence-transformers model)
4. Copy your API key to the `.env` file

### Google AI Studio Setup

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Copy the key to your `.env` file

## 📁 Project Structure

```
MedSync-AI-Chatbot/
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── src/
│   ├── helper.py            # Utility functions
│   └── prompt.py            # System prompts
├── data/                    # Medical documents (PDFs)
├── templates/               # HTML templates (legacy)
└── static/                 # Static assets (legacy)
```

## 🎯 Usage

1. **Start the application** using one of the run commands above
2. **Open your browser** to the provided URL (usually `http://localhost:8501`)
3. **Type medical questions** in the chat interface
4. **Get instant responses** from the AI-powered medical assistant

## 🔍 Features in Detail

### Chat Interface

- **Real-time messaging**: Instant responses with loading indicators
- **Message history**: Persistent chat history during session
- **Clear chat**: Option to reset conversation
- **Error handling**: Graceful error messages for failed requests

### Sidebar Information

- **About section**: Application description and features
- **Usage instructions**: How to use the chatbot
- **Disclaimer**: Medical advice disclaimer
- **Technology stack**: Information about underlying technologies

### AI Capabilities

- **Semantic search**: Finds relevant medical information
- **Context-aware responses**: Uses retrieved context for answers
- **Concise answers**: Limited to 3 sentences for clarity
- **Medical focus**: Specialized for healthcare queries

## 🚨 Important Notes

### Medical Disclaimer

⚠️ **This application is for informational purposes only and should not replace professional medical advice. Always consult with qualified healthcare professionals for medical decisions.**

### API Limits

- Be aware of your Pinecone and Gemini API usage limits
- Monitor your API consumption to avoid unexpected charges

### Data Privacy

- Ensure your medical documents are properly anonymized
- Follow HIPAA and other relevant privacy regulations
- Consider data retention policies

## 🛠️ Development

### Adding New Features

1. Modify `streamlit_app.py` for UI changes
2. Update `src/prompt.py` for system prompt changes
3. Modify `src/helper.py` for utility function changes

### Customization

- **Styling**: Modify the CSS in the `st.markdown()` section
- **Prompts**: Edit the system prompt in `src/prompt.py`
- **Model**: Change the Gemini model in the `ChatGoogleGenerativeAI` initialization

## 📊 Performance

- **Caching**: Uses Streamlit's `@st.cache_resource` for efficient resource management
- **Vector Search**: Optimized retrieval with k=3 similar documents
- **Response Time**: Typically responds within 2-5 seconds

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**:

   - Verify your API keys are correct
   - Check that the `.env` file is in the root directory
   - Ensure keys have proper permissions

2. **Pinecone Connection Issues**:

   - Verify your Pinecone index exists
   - Check that the index name matches "medical-chatbot"
   - Ensure your API key has access to the index

3. **Streamlit Not Starting**:

   - Check if port 8501 is available
   - Try a different port with `--server.port`
   - Verify all dependencies are installed

4. **Slow Responses**:
   - Check your internet connection
   - Verify API rate limits
   - Consider upgrading your API plan

## 📈 Monitoring

- **Streamlit logs**: Check the terminal for application logs
- **API usage**: Monitor your Pinecone and Gemini dashboard
- **Performance**: Watch response times in the chat interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the amazing web app framework
- **Google AI**: For the Gemini model
- **Pinecone**: For vector database services
- **LangChain**: For the RAG framework

---

**Built with ❤️ using Streamlit**
