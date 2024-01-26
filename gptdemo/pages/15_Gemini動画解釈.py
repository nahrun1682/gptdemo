import streamlit as st
from dotenv import load_dotenv
import os
import logging
import google.generativeai as genai
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import base64
from vertexai.preview.generative_models import GenerativeModel, Part

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# APIキーの設定
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
google_gemini_key = os.environ["GOOGLE_GEMINI_KEY"]
genai.configure(api_key=google_gemini_key)

# Function to encode the image to base64
def encode_image(uploaded_image):
    return base64.b64encode(uploaded_image.getvalue()).decode('utf-8')

st.title('🖼️ Gemini動画解析')


# Streamlitを使って画像をアップロードする
uploaded_file = st.file_uploader("画像を選択してください(mp4のみ対応)", type=['mp4'])
user_input = st.text_input("質問を入力してください（例：この動画には何が映っていますか？）")

if st.button('GPT4-visionに聞く'):
    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        movie_base64=base64.b64encode(file_bytes)
        movie_part = Part.from_data(data=base64.b64decode(movie_base64), mime_type="video/mp4")

        config = {
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
        }

        model = GenerativeModel(model_name="gemini-pro-vision", generation_config=config)

        response = model.generate_content(
        [movie_part, "この動画について詳しく説明してください"]
        )

        print(response.candidates[0].content.parts[0].text)
        st.text(response.candidates[0].content.parts[0].text)
      
    else:
        st.info('Please upload an image to get started.')
else:
    st.info('画像をアップロードし、質問を入力したら「解析を開始」ボタンを押してください。')
    