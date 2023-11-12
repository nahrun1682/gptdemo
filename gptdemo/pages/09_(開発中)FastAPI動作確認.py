import streamlit as st
import requests

# FastAPIサーバーのURL
fastapi_url = "http://localhost:8000"

def get_root():
    response = requests.get(f"{fastapi_url}/")
    return response.json()

def get_item(item_id, q=None):
    params = {"q": q} if q else {}
    response = requests.get(f"{fastapi_url}/items/{item_id}", params=params)
    return response.json()

st.title("FastAPI Demo with Streamlit")

# ルートエンドポイントのテスト
st.subheader("Root Endpoint")
if st.button("Get Root"):
    root_response = get_root()
    st.json(root_response)

# アイテムエンドポイントのテスト
st.subheader("Item Endpoint")
item_id = st.number_input("Enter Item ID", min_value=1, value=1)
q = st.text_input("Enter Query (optional)")
if st.button("Get Item"):
    item_response = get_item(item_id, q)
    st.json(item_response)
