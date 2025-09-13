import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import base64

# Load Environment Variables
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

# Initialize Embeddings and Vector Store
@st.cache_resource
def initialize_chatbot():
    """Initialize the chatbot components with caching for performance"""
    embeddings = download_hugging_face_embeddings()
    
    index_name = "medical-chatbot"
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
    
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    
    chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=GEMINI_API_KEY
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    question_answer_chain = create_stuff_documents_chain(chat_model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain

# Initialize the Chatbot
try:
    rag_chain = initialize_chatbot()
except Exception as e:
    st.error(f"Error initializing chatbot: {str(e)}")
    st.stop()

# Function to Get base64 Encoded Logo
@st.cache_data
def get_logo_base64():
    """Get base64 encoded logo for display"""
    try:
        with open('static/logo-single.png', 'rb') as f:
            logo_bytes = f.read()
        return base64.b64encode(logo_bytes).decode()
    except:
        return None

# Streamlit UI Configuration
st.set_page_config(
    page_title="MedSync AI - Healthcare Assistant",
    page_icon="static/logo-single.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Healthcare Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    .main-header {
        font-family: 'Inter', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #059669;
        text-align: center;
        margin-bottom: 1rem;
        letter-spacing: -0.025em;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #374151;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .logo {
        width: 80px;
        height: 80px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stChatMessage {
        background: transparent !important;
        padding: 0.5rem 0 !important;
        margin: 0 !important;
        border: none !important;
    }
    
    .stChatMessage[data-testid="chatMessage"] {
        background: transparent !important;
        padding: 0.5rem 0 !important;
        margin: 0 !important;
    }
    
    .stChatMessage .stChatMessageContent {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
    }
    
    .user-message {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 4px 18px;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        max-width: 70%;
        margin-left: auto;
        display: inline-block;
    }
    
    .assistant-message {
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        padding: 1rem 1.5rem;
        border-radius: 18px 18px 18px 4px;
        margin: 0.5rem 0;
        font-family: 'Inter', sans-serif;
        color: #374151;
        line-height: 1.6;
        max-width: 70%;
        margin-right: auto;
        display: inline-block;
    }
    
    .stChatInput {
        background: white;
        border-radius: 12px;
        border: 2px solid #e5e7eb;
        padding: 0.75rem 1rem;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        margin-top: 1rem;
    }
    
    .stChatInput:focus {
        border-color: #10b981;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .sidebar-header {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        color: #059669;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .sidebar-section {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .feature-list {
        font-family: 'Inter', sans-serif;
        color: #374151;
        line-height: 1.6;
    }
    
    .feature-list li {
        margin-bottom: 0.5rem;
        padding-left: 0.5rem;
    }
    
    .disclaimer {
        background: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-family: 'Inter', sans-serif;
        color: #92400e;
        font-size: 0.9rem;
    }
    
    .footer {
        text-align: center;
        color: #6b7280;
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #e5e7eb;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
        padding: 1rem;
        background: #f9fafb;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
    }
    
    .stat-item {
        text-align: center;
        font-family: 'Inter', sans-serif;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #059669;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #6b7280;
        margin-top: 0.25rem;
    }
    
    .chat-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 2rem;
        min-height: 500px;
        max-height: 700px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# Header With Logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    logo_base64 = get_logo_base64()
    if logo_base64:
        st.markdown(f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" class="logo"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header">MedSync AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Intelligent Healthcare Assistant</p>', unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)

# Chat Input
if prompt := st.chat_input("Ask about Medical Topics, Symptoms, or Healthcare Information..."):
    # Add User Message to Chat History
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display User Message
    with st.chat_message("user"):
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
    
    # Display Assistant Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            with st.spinner("Processing Your Request..."):
                response = rag_chain.invoke({"input": prompt})
                answer = response["answer"]
            
            message_placeholder.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
        except Exception as e:
            error_message = f"Sorry, I encountered an error: {str(e)}"
            message_placeholder.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# Side Bar
with st.sidebar:
    st.markdown('<div class="sidebar-header">MedSync AI</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-list">
        <strong>Key Features:</strong>
        <ul>
            <li>AI-powered Medical Responses</li>
            <li>Comprehensive Knowledge Base</li>
            <li>Natural Conversation Interface</li>
            <li>Real-time Information Retrieval</li>
            <li>Evidence-based Medical Guidance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-list">
        <strong>How to Use:</strong>
        <ol>
            <li>Type Your Medical Question</li>
            <li>Press Enter or Click Send</li>
            <li>Receive Instant Medical Information</li>
            <li>Ask Follow-up Questions as Needed</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-list">
        <strong>Powered by:</strong>
        <ul>
            <li>Google Gemini AI</li>
            <li>Pinecone Vector Database</li>
            <li>Streamlit Framework</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)