import streamlit as st
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

#ワイド表示
st.set_page_config(layout="wide")

#タイトルを表示
st.title('🦜ChatGPT@２デジ(デモ用)')
st.subheader("StreamlitというAI/ML用のフロント開発ライブラリを使ってます")

#セレクトボックスのリストを作成
# pagelist = ["ChatGPT","社内文書検索GPT(デモ)","TownPageGPT(デモ)"]
# #サイドバーのセレクトボックスを配置
# selector=st.sidebar.radio( "好きなGPTを選択",pagelist)
# if selector=="page1":
#     if st.button('社内文書検索GPT(デモ)'):
#         st.title("社内文書検索GPT(デモ)")
# elif selector=="page2":
#     if st.button('TownPageGPT(デモ)'):
#         st.title("TownPageGPT(デモ)")
#アプリはユーザーから OpenAI API キーを受け取り、それを使用して応答を生成します。
#openai_api_key = st.sidebar.text_input('OpenAI API Key')
#openai_api_key = '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'
openai_api_key = os.environ["OPENAI_API_KEY"]

#テキストの一部を入力として受け取り、このメソッドを使用してOpenAI()AI 生成コンテンツを生成し、次を使用して青いボックス内にテキスト出力を表示します
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

#最後に、st.form() を使用して、ユーザーが入力したプロンプトを受け入れるためのテキストボックス (st.text_area()) を作成します。
#ユーザーが「送信」ボタンをクリックした時点で、prompt 入力変数 (テキスト) を引数として、generate-response() 関数が呼び出されます。
with st.form('my_form'):
  text = st.text_area('Enter text:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)