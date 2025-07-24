
import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import time
import os

# Set up page
st.set_page_config(page_title="CanWeTalk - Speak English", layout="centered", page_icon="🎙️")

st.title("🗣️ CanWeTalk – Speak English Fluently")
st.markdown("Speak in Hindi or broken English, and get the correct English sentence back with voice.")

# Translator
translator = Translator()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=5)
            st.success("✅ Speech Captured")
            return r.recognize_google(audio, language='hi-IN')  # Use Hindi model
        except sr.UnknownValueError:
            st.warning("Couldn't understand. Try again.")
        except sr.RequestError:
            st.error("Speech Recognition service error.")
        except sr.WaitTimeoutError:
            st.warning("No voice detected.")
    return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    path = "response.mp3"
    tts.save(path)
    time.sleep(1)  # wait 1 sec before speaking
    audio_file = open(path, 'rb')
    st.audio(audio_file.read(), format='audio/mp3')
    audio_file.close()
    os.remove(path)

# Button to start speaking
if st.button("🎙️ Speak Now"):
    spoken_text = listen()
    if spoken_text:
        st.subheader("📝 You Said:")
        st.write(spoken_text)

        # Translate to English
        result = translator.translate(spoken_text, dest='en')
        st.subheader("✅ Correct English:")
        st.write(result.text)

        st.subheader("🔊 Listening:")
        speak(result.text)
