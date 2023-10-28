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
- [9. 宿題](#9-宿題)

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

# 9. 宿題

1. ストリーム処理をlangcahinから
2. langcahinからazureへ
3. dockerによるコンテナ化
4. jupyter vscode上で使いたいよね