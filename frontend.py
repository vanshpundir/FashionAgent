import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration with a more modern layout
st.set_page_config(
    page_title="AI Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with modern styling
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Header Styling */
    h1 {
        color: #1a1a1a;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 2rem !important;
        padding-top: 1rem;
    }
    
    /* Chat Container */
    .chat-message {
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        max-width: 85%;
    }
    
    .chat-message.user {
        background-color: #e9ecef;
        margin-left: auto;
        border-bottom-right-radius: 0.5rem;
    }
    
    .chat-message.assistant {
        background-color: white;
        margin-right: auto;
        border-bottom-left-radius: 0.5rem;
    }
    
    .chat-message.tool {
        background-color: #e3f2fd;
        margin: 1rem auto;
        width: 95%;
    }
    
    /* Tool Calls Styling */
    .tool-call {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 0.8rem;
        font-family: 'IBM Plex Mono', monospace;
        border: 1px solid #e0e0e0;
    }
    
    .tool-response {
        background-color: rgba(244, 245, 246, 0.9);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 0.8rem;
        font-family: 'IBM Plex Mono', monospace;
        border: 1px solid #e0e0e0;
    }
    
    /* Input Area Styling */
    .stTextInput input {
        border: 2px solid #e0e0e0;
        border-radius: 0.75rem;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput input:focus {
        border-color: #19C37D;
        box-shadow: 0 0 0 2px rgba(25, 195, 125, 0.1);
    }
    
    /* Button Styling */
    .stButton button {
        background-color: #19C37D;
        color: white;
        border-radius: 0.75rem;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    div.stButton > button:hover {
        background-color: #128c5e;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Clear Chat Button */
    .clear-button {
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 1000;
    }
    
    /* Message Content */
    .message {
        line-height: 1.5;
        font-size: 1rem;
    }
    
    .message b {
        color: #1a1a1a;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Code Blocks */
    pre {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        overflow-x: auto;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Rest of the functions remain the same
def format_json(json_str):
    try:
        if isinstance(json_str, str):
            data = json.loads(json_str)
        else:
            data = json_str
        return json.dumps(data, indent=2)
    except:
        return json_str

def process_tool_calls(tool_calls):
    html = ""
    for call in tool_calls:
        function_name = call['function']['name']
        arguments = format_json(call['function']['arguments'])
        html += f"""
        <div class="tool-call">
            <b>Tool Call:</b> {function_name}<br>
            <b>Arguments:</b><br>
            <pre>{arguments}</pre>
        </div>
        """
    return html

def process_tool_responses(tool_responses):
    html = ""
    for response in tool_responses:
        content = format_json(response['content'])
        html += f"""
        <div class="tool-response">
            <b>Tool Response:</b><br>
            <pre>{content}</pre>
        </div>
        """
    return html

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

def generate_response(prompt):
    url = "http://localhost:8010/generate"
    headers = {'Content-Type': 'application/json'}
    data = {"query": prompt}
    
    try:
        response = requests.get(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def display_message(message):
    role = message.get('role', 'user')
    content = message.get('content')
    tool_calls = message.get('tool_calls', [])
    tool_responses = message.get('tool_responses', [])
    
    if not content and not tool_calls and not tool_responses:
        return
    if content == "TERMINATE":
        return
        
    if message.get('name') == 'chatbot':
        role = 'assistant'
    display_name = "Assistant" if role == 'assistant' else ("Tool" if role == 'tool' else "You")
    
    message_html = f"""<div class="chat-message {role}"><div class="message">"""
    
    if content:
        message_html += f"<b>{display_name}</b><br>{content}<br>"
    
    if tool_calls:
        message_html += process_tool_calls(tool_calls)
    
    if tool_responses:
        message_html += process_tool_responses(tool_responses)
    
    message_html += "</div></div>"
    st.markdown(message_html, unsafe_allow_html=True)

# Main title
st.title("AI Assistant")

# Chat container with padding
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.messages:
        display_message(message)

# User input form with improved layout
with st.container():
    col1, col2 = st.columns([4, 1])
    
    with st.form(key='message_form', clear_on_submit=True):
        user_input = st.text_input("Message", key='user_input', placeholder="Type your message here...")
        cols = st.columns([1, 1, 1, 1])
        with cols[3]:
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })
            
            response = generate_response(user_input)
            if response and 'result' in response:
                chat_history = response['result'].get('chat_history', [])
                for msg in chat_history:
                    st.session_state.messages.append(msg)
                
                st.rerun()

# Clear chat button in top right corner
with st.container():
    col1, col2, col3 = st.columns([6, 6, 1])
    with col3:
        if st.button("Clear", key="clear_chat"):
            st.session_state.messages = []
            st.rerun()