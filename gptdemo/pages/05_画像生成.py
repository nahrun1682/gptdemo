import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
import os

# Streamlitアプリのタイトル
st.title("DALL-E 画像生成アプリ")

# APIキーの設定（環境変数から取得することを推奨）
openai.api_key = os.environ["OPENAI_API_KEY"]

# DALL-Eによる画像生成関数
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1, # 1〜10枚まで設定できる
        # 三つのサイズを選択できる
        #size = "256x256",
        #size = "512x512",
        size="1024x1024"
)
    return response['data'][0]['url']

# ユーザー入力フィールド
user_input = st.text_input("画像を生成したいテキストを入力してください", "赤いリンゴ")

# 画像生成ボタン
if st.button("画像生成"):
    # 画像を生成
    image_url = generate_image(user_input)

    # 画像を表示
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    st.image(img)

