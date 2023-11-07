import streamlit as st
import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
# 環境変数からOpenAI API Keyを取得
openai_api_key = os.environ["OPENAI_API_KEY"]

# Function to encode the image to base64
def encode_image(uploaded_image):
    return base64.b64encode(uploaded_image.getvalue()).decode('utf-8')

st.title('🖼️ OpenAI Image Response')

# Streamlitを使って画像をアップロードする
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Encode the image to base64
    base64_image = encode_image(uploaded_file)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "これはなんの画像ですか？日本語で回答してください"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    # APIへのPOSTリクエストを行い、レスポンスを得る
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    # デバッグのために応答をプリント
    print(response.json())
    
    # レスポンスを確認してStreamlitに表示
    if response.status_code == 200:
        response_data = response.json()
        assistant_message = response_data['choices'][0]['message']['content']
        if assistant_message:
            st.text_area("AI's response:", assistant_message, height=300)
    else:
        st.error("Failed to call OpenAI API")
else:
    st.info('Please upload an image to get started.')
    

