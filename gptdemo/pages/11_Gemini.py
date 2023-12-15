import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# APIキーの設定
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
google_gemini_key=os.environ["GOOGLE_GEMINI_KEY"]
genai.configure(api_key=google_gemini_key)

# Streamlitのインターフェース設定
st.title('😱Generative AI with Google API')
user_input = st.text_input("Enter your question:")

if user_input:
    # モデルの設定
    model = genai.GenerativeModel('gemini-pro')

    # ユーザーの入力をモデルに渡す
    response = model.generate_content(user_input)

    # 結果を表示
    st.write(response.text)