import streamlit as st
import time

# --- Page Config ---
st.set_page_config(page_title="TalkBot Pro | Enterprise Conversational AI", page_icon="💬", layout="centered")

# --- Custom CSS for Chat Interface ---
st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .chat-bubble {
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 15px;
        max-width: 80%;
    }
    .bot-bubble {
        background-color: #ffffff;
        color: #1a202c;
        border-bottom-left-radius: 5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .user-bubble {
        background-color: #3b82f6;
        color: white;
        align-self: flex-end;
        margin-left: auto;
        border-bottom-right-radius: 5px;
    }
    .stTextInput input { border-radius: 25px !important; }
</style>
""", unsafe_allow_html=True)

# --- State Init ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI Business Assistant. How can I help you today?"}
    ]

# --- Sidebar ---
with st.sidebar:
    st.title("🤖 TalkBot Config")
    st.markdown("---")
    st.subheader("Knowledge Base")
    st.file_uploader("Upload Company PDF/Doc", type=["pdf", "txt", "docx"])
    st.divider()
    st.subheader("Model Settings")
    st.select_slider("Creativity (Temperature)", options=["Strict", "Balanced", "Creative"], value="Balanced")
    st.success("Status: **Active**")

# --- Header ---
st.markdown("<h1 style='text-align:center; color:#1e293b;'>TalkBot Pro AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b;'>Advanced Customer Support Simulation</p>", unsafe_allow_html=True)
st.divider()

# --- Chat Display ---
for msg in st.session_state.messages:
    side = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(f'<div class="chat-bubble {side}">{msg["content"]}</div>', unsafe_allow_html=True)

# --- Chat Input ---
user_input = st.chat_input("Ask me about our services or pricing...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.rerun()

# --- AI Logic Simulation ---
if st.session_state.messages[-1]["role"] == "user":
    with st.spinner("AI is thinking..."):
        time.sleep(1.5)
        response = "That's a great question! Based on my knowledge base, we offer 24/7 support and our pricing starts at just $19.99/month. Would you like to see a full comparative breakdown?"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
