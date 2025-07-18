import openai
import streamlit as st

# Load API key securely
openai.api_key = st.secrets["openai_api_key"]

# Initialize session state to store conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = [{"role": "system", "content": "You are a supportive mental health assistant that provides encouragement, stress relief advice, and mental health suggestions."}]

def respond_with_gpt(user_input):
    # Append user message
    st.session_state.conversation.append({"role": "user", "content": user_input})
    
    # Create response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.conversation
    )

    # Extract and store assistant reply
    reply = response['choices'][0]['message']['content']
    st.session_state.conversation.append({"role": "assistant", "content": reply})
    return reply
