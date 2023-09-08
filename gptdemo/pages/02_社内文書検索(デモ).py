import streamlit as st
from langchain.llms import OpenAI
import os

st.title('🦜ChatGPT@２デジ(デモ用)')
st.subheader("社内文書検索GPT(デモ)")

openai_api_key = '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'
os.environ["OPENAI_API_KEY"]=openai_api_key