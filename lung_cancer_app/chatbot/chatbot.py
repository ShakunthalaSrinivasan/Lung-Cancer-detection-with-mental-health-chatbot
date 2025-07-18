import openai
import streamlit as st

openai.api_key = st.secrets["openai_api_key"]
conversation = []

def respond_with_gpt(user_input):
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    reply = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": reply})
    return reply
