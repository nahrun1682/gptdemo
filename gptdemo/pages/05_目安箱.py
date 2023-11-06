import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
gmail_password = os.environ["gmail_password"]

# ユーザー入力用のフォームを作成
with st.form(key='my_form'):
    email = st.text_input("メールアドレス")
    idea = st.text_area("あなたのアイデアをここに記入してください")
    submit_button = st.form_submit_button(label='送信')

# 送信ボタンが押されたら
if submit_button:
    # Gmailの認証情報
    username = 'kawamura100995@gmail.com'
    # gmail_password = '生成したアプリパスワード'  # 2段階認証を設定している場合はアプリパスワードが必要

    # メールの内容を設定
    message = MIMEMultipart()
    message['From'] = email
    message['To'] = username  # 送信先のメールアドレス（自分自身）
    message['Subject'] = '新しいアイデアの提案'

    # メールの本文
    body = f"送信者メール: {email}\n送信内容:\n{idea}"
    message.attach(MIMEText(body, 'plain'))

    # GmailのSMTPサーバーを使ってメールを送信
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, gmail_password)
    text = message.as_string()
    server.sendmail(email, username, text)
    server.quit()

    # 送信完了のメッセージ
    st.success("アイデアを送信しました！")
