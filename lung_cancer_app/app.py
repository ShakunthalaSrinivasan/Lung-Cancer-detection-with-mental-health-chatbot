import streamlit as st
from chatbot.gpt_chatbot import respond_with_gpt
from chatbot.mood_logger import log_mood_to_db
from detector.predict import predict_lung_cancer
from datetime import datetime
import PIL

st.set_page_config(page_title="Lung Health Companion", layout="centered")

menu = st.sidebar.selectbox("Choose Module", ["🏥 Lung Cancer Detection", "🧠 Mental Health Chatbot"])

if menu == "🏥 Lung Cancer Detection":
    st.title("Lung Cancer Detection")
    st.write("Upload a histopathology image for cancer prediction.")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Predict"):
            prediction = predict_lung_cancer(image)
            st.success(f"Prediction: **{prediction}**")

elif menu == "🧠 Mental Health Chatbot":
    st.title("🧠 Mental Health Support Chatbot")

    name = st.text_input("Your Name:")
    mood = st.selectbox("How are you feeling today?", ["☺️ Happy", "😞 Sad", "😠 Angry", "😰 Anxious", "😐 Neutral"])
    if st.button("Log Mood"):
        if name:
            log_mood_to_db(name, mood)
            st.success("✅ Mood logged.")
        else:
            st.warning("Please enter your name.")

    st.markdown("### Talk to the chatbot")
    user_input = st.text_input("You:")
    if user_input:
        if any(word in user_input.lower() for word in ["give up", "end it", "die"]):
            st.error("⚠️ You're not alone. Please seek professional help.")
            st.markdown("[🆘 iCall Helpline](https://www.icallhelpline.org/)")
        reply = respond_with_gpt(user_input)
        st.markdown(f"**Bot:** {reply}")

    st.markdown("### Quick Help")
    if st.button("Help with anxiety"):
        reply = respond_with_gpt("I'm feeling anxious. Please help.")
        st.write(reply)
