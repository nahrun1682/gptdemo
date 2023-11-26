# 1. デモ用フロント画面

# 2. 目次

- [1. デモ用フロント画面](#1-デモ用フロント画面)
- [2. 目次](#2-目次)
- [3. 前提](#3-前提)
- [4. 使い方](#4-使い方)
- [5. プロキシ環境](#5-プロキシ環境)
- [6. Azure App ServicesでのStreamlitアプリのデプロイ](#6-azure-app-servicesでのstreamlitアプリのデプロイ)
- [7. Azure App Service で実行されている Web アプリにアプリの認証を追加する](#7-azure-app-service-で実行されている-web-アプリにアプリの認証を追加する)
- [8. Poetryコマンド](#8-poetryコマンド)
- [9. Docker](#9-docker)
- [10. k8s](#10-k8s)
- [11. fastapi+gunicorn](#11-fastapigunicorn)
- [12. 宿題](#12-宿題)
- [13. スタートアップコマンド](#13-スタートアップコマンド)

# 3. 前提 

# 4. 使い方

```zsh
#gptdemo配下に移動
cd gptdemo 

#仮想環境起動
poetry install
#フロント起動
poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py
```

成功すると以下が標準出力される
```zsh
/mnt/d/GPT/gptdemo % poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.18.62.148:8501

gio: http://localhost:8501: Operation not supported

```

そしたら、http://localhost:8501
へ遷移

# 5. プロキシ環境

参考：[プロキシ環境でのPython環境構築まとめ](https://qiita.com/c60evaporator/items/7a757134d028a7734118)

プロジェクト内のpyproject.tomlに以下の記述を追加

```zsh
[[tool.poetry.source]]
name = "proxy"
url = "http://プロキシのアドレス:ポート"
default = true
```

# 6. Azure App ServicesでのStreamlitアプリのデプロイ
参考[Azure App ServicesでのStreamlitアプリのデプロイ](https://docs.kanaries.net/ja/tutorials/Streamlit/deploy-streamlit-app)

[Azure App ServiceへのPython Webアプリの簡単デプロイ（CLI）](https://qiita.com/yakigac/items/a3369bfc2f4730cd299f)

Azure App ServicesにStreamlitアプリをデプロイする手順のガイドを以下に示します。

1. Azureアカウントの作成：まだ持っていない場合、Azureアカウントにサインアップしてください。

1. 新しいApp Serviceの作成：Azureポータルに移動し、新しいApp Serviceを作成します。

1. App Serviceの構成：サブスクリプション、リソースグループ、名前、公開方法（コード）、ランタイムスタック（Python）、およびオペレーティングシステムを選択します。

1. アプリをデプロイする：App Serviceが設定されたら、Azure CLIまたはGitを使用してStreamlitアプリをデプロイできます。Azure CLIを使用してアプリをデプロイするためのサンプルコマンドのシーケンスを以下に示します。

```zsh
az webapp up --sku F1 --name my-streamlit-app
```

これらの手順の後、StreamlitアプリはAzure App Services上で公開されるはずです。

# 7. Azure App Service で実行されている Web アプリにアプリの認証を追加する

参考：[チュートリアル: Azure App Service で実行されている Web アプリにアプリの認証を追加する](https://learn.microsoft.com/ja-jp/azure/app-service/scenario-secure-app-authentication-app-service)



# 8. Poetryコマンド

参考:[Poetryをサクッと使い始めてみる](https://qiita.com/ksato9700/items/b893cf1db83605898d8a)
インストールされているパッケージのアップグレード（バージョンアップ）を行いたい時には poetry updateを使う。

```zsh
poetry update --dry-run
#とするとアップグレードされるパッケージがわかるので、それを確認した上で
poetry update
```
すると実際にアップグレードが行われます。なお、poetry updateした時に変更されるのはpoetry.lockだけで pyproject.tomlはそのままです。新しいバージョンの新機能を使うなどの場合はpyproject.tomlを手動で修正してして依存するバージョンを変える必要があります。

# 9. Docker
ローカル環境でDockerコンテナをビルドして実行するには、以下の手順を実行する必要があります。これにより、アプリケーションがコンテナ内でどのように動作するかを確認できます。以下のコマンドは、プロジェクトのルートディレクトリ（`Dockerfile`が存在する場所）で実行することを想定しています。

1. **Dockerイメージのビルド:**
    最初に、Dockerイメージをビルドする必要があります。これにより、アプリケーションのスナップショットが作成され、それを実行するための環境が設定されます。以下のコマンドを使用します。

    ```sh
    docker build -t gptdemo .
    ```

    ここで、`my-python-app`は作成するDockerイメージに付ける名前です（任意の名前を使用できます）。また、最後の`.`は`Dockerfile`とコンテキスト（コピーするファイルなど）が現在のディレクトリにあることを指します。

2. **コンテナの実行:**
    イメージがビルドされたら、新しいコンテナインスタンスを起動することができます。アプリケーションがウェブサーバーを使用している場合、適切なポートを公開する必要があります。

    ```bash
    docker run --name mygptdemo -p 8501:8080 gptdemo
    ```

    このコマンドは、ローカルマシンのポート8501をコンテナのポート8501にバインドします（Streamlitがデフォルトで使用）。`my-python-app`は、先ほどビルドしたDockerイメージの名前です。

    もしアプリケーションが異なるポートを使用する場合、`-p`フラグのパラメータをそのポート番号に変更する必要があります（例：`-p 8080:8080`）。

3. **アプリケーションの確認:**
    コンテナが実行されたら、ウェブブラウザを開いて `http://localhost:8501` （または選択したポート番号に応じて適切なURL）にアクセスします。アプリケーションが正しく実行されていれば、そのインターフェースが表示されます。

このプロセスにより、Dockerコンテナの中でアプリケーションがどのように動作するかをローカル環境で確認できます。これはデプロイ前のテストやデバッグ、開発プロセス中の問題のトラブルシューティングに非常に役立ちます。

4. **アクセス**
   http://localhost:8501

# 10. k8s



# 11. fastapi+gunicorn

```bash
#起動方法
poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.main:app
```


# 12. 宿題

1. ストリーム処理をlangcahinから
2. langcahinからazureへ
3. dockerによるコンテナ化
4. jupyter vscode上で使いたいよね
5. pip install poetry && poetry install && poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port $PORT
6. /mnt/d/GPT/GPTDEMO # poetry --version
Poetry (version 1.7.0)

# 13. スタートアップコマンド
pip install --upgrade pip && \
pip install poetry==1.7.0 && \  # ここで特定のpoetryバージョンを指定
poetry config virtualenvs.create false --local && \  # システムのPython環境を使用
poetry install --no-interaction --no-ansi && \
poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port $PORT


pip install --upgrade pip && pip install poetry==1.7.0 && poetry config virtualenvs.create false --local && poetry install --no-interaction --no-ansi && poetry update langchain && poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port $PORT

```bash
#20231112(動いた)
pip install poetry && poetry install && poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port $PORT

#20231112()
pip install poetry && poetry install & poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.main:app --bind 0.0.0.0:8000

#以下エラー
2023-11-12T15:01:47.956Z INFO  - docker run -d --expose=8181 --expose=8082 --name gpt-demo-stremlit_0_eeaa3578_middleware -e WEBSITE_AUTH_ENABLED=True -e PORT=80 -e WEBSITE_SITE_NAME=gpt-demo-stremlit -e WEBSITE_ROLE_INSTANCE_ID=0 -e WEBSITE_HOSTNAME=gpt-demo-stremlit.azurewebsites.net -e WEBSITE_INSTANCE_ID=854dd9506899c9694307e0d08f4d78a285a46de0e3c0d6c64653dc76fa8620f8 -e HTTP_LOGGING_ENABLED=1 -e WEBSITE_USE_DIAGNOSTIC_SERVER=False mcr.microsoft.com/appsvc/middleware:stage5 /Host.ListenUrl=http://0.0.0.0:8181 /Host.DestinationHostUrl=http://169.254.129.2:80 /Host.UseFileLogging=true
```

```bash
sh startup.sh
```

```bash
echo "Starting setup..." ; \
echo "Installing dependencies..." ; pip install poetry ; poetry install ; \
echo "Starting Streamlit application..." ; poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port 80 & \
echo "Starting FastAPI application..." ; poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.main:app --bind 0.0.0.0:8000 & ; \
echo "Startup script completed."
```

#雑記

```python
メモ　非同期処理

import multiprocessing
import time
import os
from dotenv import load_dotenv
import streamlit as st

from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage

# .envファイルの読み込み
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
openai_api_key = os.environ["OPENAI_API_KEY"]

class LLMWorker(multiprocessing.Process):
    def __init__(self, openai_api_key, model_name, temperature, messages, **kwargs):
        super().__init__(**kwargs)
        self.openai_api_key = openai_api_key
        self.model_name = model_name
        self.temperature = temperature
        self.messages = messages
        self.response = multiprocessing.Queue(1)

    def run(self):
        llm = ChatOpenAI(openai_api_key=self.openai_api_key, model_name=self.model_name, temperature=self.temperature)
        response = llm(self.messages)
        self.response.put(response)

def main():
    st.title('🦜ChatGPT DEMO')

    with st.sidebar:
        st.header('設定')
        with st.expander("モデル選択"):
            model_name = st.radio(
                "モデルを選択(1106が現在最新版):",
                ("gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-1106", "gpt-4-1106-preview"),
                index=3
            )
        with st.expander("オプション設定"):
            temperature = st.slider(
                "Temperature(大きいほど正確、低いほどランダム):", 
                min_value=0.0, max_value=1.0, value=1.0, step=0.1
            )

    if "messages" not in st.session_state:
        st.session_state["messages"] = [ChatMessage(role="assistant", content="なんでも聞いてね")]

    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)

    if prompt := st.chat_input():
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))
        st.chat_message("user").write(prompt)

        worker = LLMWorker(openai_api_key, model_name, temperature, st.session_state.messages, daemon=True)
        worker.start()

        while worker.is_alive():
            time.sleep(0.1)

        response = worker.response.get()
        st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))
        worker.join()

if __name__ == '__main__':
    main()

```

以下はstreamしつつ非同期処理

```python
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st
import asyncio

st.set_page_config(layout="wide")
async def manual_run(panel, llm, prompt_template, memory, question):
    message = prompt_template.format_prompt(
        human_input=question, 
        chat_history=memory.load_memory_variables({})["chat_history"]
    )
    # add to ui
    with panel:
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            container = st.empty()

    response = ""
    async for chunk in llm.astream(message):
        response += chunk.content
        container.markdown(response)

    memory.save_context({"input": question}, {"output": response})
    return response


async def logic(location, key, panel):
    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0.2, max_tokens=512, streaming=True)
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ])
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    questions = [
        "こんにちは",
        f"{location}の観光名所を教えて",
        f"この観光名所の{location}駅からの行き方は？"
    ]
    answers = []
    for question in questions:
        # Add to state
        st.session_state[f"messages{key}"].append({
            "role": "user",
            "content": question
        })
        # run chatgpt
        ans = await manual_run(panel, llm, prompt, memory, question)
        # add to state
        st.session_state[f"messages{key}"].append({
            "role": "assistant",
            "content": ans
        })
        answers.append(ans)
    return answers

async def task_factory(parameters):
    tasks = []
    for param in parameters:
        t = asyncio.create_task(logic(*param))
        tasks.append(t)
    return await asyncio.gather(*tasks)

def main():
    if "messages1" not in st.session_state:
        st.session_state.messages1 = []
        st.session_state.messages2 = []

    st.title("Multiple Streaming Chat")

    column_left, column_right = st.columns(2)
    button = st.button("Click to start chats")

    with column_left:
        for message in st.session_state.messages1:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    with column_right:
        for message in st.session_state.messages2:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if button:
        parameters = [
            ("東京", 1, column_left),
            ("京都", 2, column_right)
        ]

        asyncio.run(task_factory(parameters))

if __name__ == "__main__":
    main()

```

以下はシンプル版
```python
import asyncio
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
import streamlit as st

st.set_page_config(layout="wide")

async def manual_run(panel, llm, prompt_template, memory, question):
    message = prompt_template.format_prompt(
        human_input=question, 
        chat_history=memory.load_memory_variables({})["chat_history"]
    )
    with panel:
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            container = st.empty()

    response = ""
    async for chunk in llm.astream(message):
        response += chunk.content
        container.markdown(response)

    memory.save_context({"input": question}, {"output": response})
    return response

async def logic(panel):
    llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0.2, max_tokens=512, streaming=True)
    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ])
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt_input := st.chat_input():
        st.session_state.messages.append({
            "role": "user",
            "content": prompt_input
        })
        ans = await manual_run(panel, llm, prompt, memory, prompt_input)
        st.session_state.messages.append({
            "role": "assistant",
            "content": ans
        })

def main():
    st.title("Simple Chat with GPT")
    asyncio.run(logic(st.container()))

if __name__ == "__main__":
    main()
```
