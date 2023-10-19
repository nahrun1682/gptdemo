import streamlit as st
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

#libsフォルダの中にあるaoai_test.pyをimport
from libs.aoai_test import generate_response_aoai

#ワイド表示
st.set_page_config(layout="wide")

#タイトルを表示
st.title('🦜ChatGPT@２デジ(デモ用)')
st.subheader("StreamlitというAI/ML用のフロント開発ライブラリを使ってます")
st.subheader("何かあればYuto.Kawamura@jp.nttdata.comまで")

#最後に、st.form() を使用して、ユーザーが入力したプロンプトを受け入れるためのテキストボックス (st.text_area()) を作成します。
#ユーザーが「送信」ボタンをクリックした時点で、prompt 入力変数 (テキスト) を引数として、generate-response() 関数が呼び出されます。
with st.form('my_form'):
  text = st.text_area('Enter text:', '')
  submitted = st.form_submit_button('Submit')
  if submitted:
    answer = generate_response_aoai(text)
    st.info(answer)