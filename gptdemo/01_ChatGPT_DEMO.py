import os
from dotenv import load_dotenv
import streamlit as st

from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
#import langchain

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
openai_api_key = os.environ["OPENAI_API_KEY"]

#langchain.verbose = False

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

#タイトルを表示
st.title('🦜ChatGPT DEMO')


    
# model_name = st.radio(label='モデルを選択してね',
#                  options=('gpt-3.5-turbo', 'gpt-4'),
#                  index=0,
#                  horizontal=True,
# )
model_name = st.sidebar.radio("モデルを選択(1106が現在最新版):", ("gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-1106","gpt-4-1106-preview"))
temperature = st.sidebar.slider("Temperature(大きいほど正確、低いほどランダム):", min_value=0.0, max_value=1.0, value=1.0, step=0.1)

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

if "messages" not in st.session_state:
    st.session_state["messages"] = [ChatMessage(role="assistant", content="なんでも聞いてね")]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(openai_api_key=openai_api_key, model_name=model_name,temperature=temperature,streaming=True, callbacks=[stream_handler])
        # print(model_name)
        response = llm(st.session_state.messages)
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))

