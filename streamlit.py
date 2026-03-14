import streamlit as st
from main import CustomerSupportChatbot

# Initialize the chatbot
try:
    chatbot = CustomerSupportChatbot()
except ValueError as e:
    st.error(str(e))
    st.stop()

st.set_page_config(page_title="Groq Customer Support Chatbot")
st.title("Customer Support Chatbot (Groq)")

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and empathetic customer support agent. Please provide concise and helpful resolutions or next steps. Start your response with 'Hello! Thank you for contacting customer support.'"}
    ]

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display the system message directly in the chat window
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is your complaint?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    with st.spinner("Thinking..."):
        full_response = chatbot.get_resolution(st.session_state.messages)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})