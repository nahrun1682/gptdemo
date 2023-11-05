import openai
from dotenv import load_dotenv
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import os

# .envファイルの読み込み
load_dotenv()
# Replace with your OpenAI API key
API_KEY = os.environ["OPENAI_API_KEY"]

def transcribe_audio_to_text(audio_bytes):
    openai.api_key = API_KEY
    with NamedTemporaryFile(delete=True, suffix=".wav") as temp_file:
        temp_file.write(audio_bytes)
        temp_file.flush()
        with open(temp_file.name, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
    return response["text"]

def audio_recorder():
    #  初期化
    if "audio_list" not in st.session_state:
        st.session_state.audio_list = []

    audio_bytes = False
    audio_bytes = audio_recorder()
    if audio_bytes:
        st.session_state.audio_list.append(audio_bytes)

    with st.sidebar:
        st.write("# 🎙️録った音")
        if st.session_state.audio_list:

            for audio_bytes in st.session_state.audio_list:
                st.audio(audio_bytes, format="audio/wav")
                
# Example usage with Streamlit:
def main():
    st.title("Voice to Text Transcription")
    
    # Record audio using Streamlit widget
    audio_bytes = audio_recorder(pause_threshold=30)
    
    # Convert audio to text using OpenAI Whisper API
    # if audio_bytes:
    #     transcript = transcribe_audio_to_text(audio_bytes)
    #     st.write("Transcribed Text:", transcript)

if __name__ == "__main__":
    audio_recorder()
