#reference:https://zenn.dev/nishijima13/articles/3b1a50b8728261
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from langchain.llms import AzureOpenAI
import openai

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

#os.environで.envファイルにある環境変数を取得
aoai_api_type = os.environ["AOAI_API_TYPE"]
aoai_api_version = os.environ["AOAI_API_VERSION"]
aoai_api_base_url = os.environ["AOAI_API_BASE_URL"]
aoai_api_key = os.environ["AOAI_API_KEY"]
aoai_deployment_name = os.environ["AOAI_DEPLOYMENT_NAME"]
openai.api_key = os.environ["OPENAI_API_KEY"]

def simple_response_chatgpt(
    user_msg: str,
):
    """ChatGPTのレスポンスを取得

    Args:
        user_msg (str): ユーザーメッセージ。
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_msg},
        ],
        stream=True,
    )
    return response