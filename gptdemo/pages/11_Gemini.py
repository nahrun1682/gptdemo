import streamlit as st
from dotenv import load_dotenv
import os
import logging
import google.generativeai as genai
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# APIキーの設定
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
google_gemini_key = os.environ["GOOGLE_GEMINI_KEY"]
genai.configure(api_key=google_gemini_key)

# Streamlitのセッションステートの初期化
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [ChatMessage(role="assistant", content="なんでも聞いてね")]

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

# Streamlitのインターフェース設定
# st.title('😱Generative AI with Google API')

# for msg in st.session_state.messages:
#     st.chat_message(msg.role).write(msg.content)

# if prompt := st.chat_input():
#     st.session_state.messages.append(ChatMessage(role="user", content=prompt))
#     st.chat_message("user").write(prompt)

#     with st.chat_message("assistant"):
#         try:
#             #stream_handler = StreamHandler(st.empty())
#             llm = ChatGoogleGenerativeAI(model="gemini-pro")
#             print(st.session_state.messages)
#             # contentとroleを取り出して結合
#             formatted_messages = ["[{}]: {}".format(message.role, message.content) for message in st.session_state.messages]

#             # 一つの文字列に結合
#             joined_string = "\n".join(formatted_messages)

#             print(joined_string)
#             response = llm.invoke(joined_string)
#             st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
#         except Exception as e:
#             logger.error(f"エラーが発生しました: {e}", exc_info=True)
#             st.error(f"エラーが発生しました: {e}")

# Streamlitのインターフェース設定
st.title('😱Generative AI with Google API')

# 既存のメッセージを表示
for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

# ユーザー入力の処理
if prompt := st.chat_input():
    # ユーザーのメッセージを追加
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))

    # AIモデルで応答を生成
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        formatted_messages = ["[{}]: {}".format(message.role, message.content) for message in st.session_state.messages]
        joined_string = "\n".join(formatted_messages)
        response = llm.invoke(joined_string)
        
        # AIの応答をメッセージリストに追加
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
        st.error(f"エラーが発生しました: {e}")

# メッセージの表示を更新
for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

