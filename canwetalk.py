import streamlit as st
from gtts import gTTS
from googletrans import Translator
import time
import os

st.set_page_config(page_title="CanWeTalk - Speak English", layout="centered", page_icon="🎙️")

st.title("🗣️ CanWeTalk – Speak English Fluently")
st.markdown("Type in Hindi (or broken English), and get correct English translation with voice.")

translator = Translator()

def speak(text):
    tts = gTTS(text=text, lang='en')
    path = "response.mp3"
    tts.save(path)
    time.sleep(1)
    with open(path, 'rb') as audio_file:
        st.audio(audio_file.read(), format='audio/mp3')
    os.remove(path)

user_input = st.text_area("✍️ Type your sentence here (Hindi or broken English):", height=100)

if st.button("🔁 Translate"):
    if user_input.strip():
        result = translator.translate(user_input, dest='en')
        st.subheader("✅ Correct English:")
        st.write(result.text)

        st.subheader("🔊 Listening:")
        speak(result.text)
    else:
        st.warning("Please enter something to translate.")
