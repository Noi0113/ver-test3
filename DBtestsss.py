import subprocess
import sqlite3
import streamlit as st
import os

st.title('確認!!!!!')
# StreamlitのWebサイトで入力された情報を取得
user_input = st.text_input('Enter your data')

# データベースに書き込み
conn = sqlite3.connect('test-monketsu3.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user_inputs (input TEXT)")
c.execute("INSERT INTO user_inputs VALUES (?)", (user_input,))
conn.commit()
conn.close()



try:
    # 現在のリポジトリが存在するリポジトリに移動
    current_directory = os.getcwd()

    # もしリポジトリが存在していなければそのリポジトリのクローンを作成
    if not os.path.exists('.git'):
        subprocess.run(['git', 'clone', 'https://github.com/Noi0113/ver-test3.git'], check=True)
        current_directory = os.getcwd()

    # DBの変更を追加する
    subprocess.run(['git', 'add', '.'], check=True)

    # 変更をコミット
    subprocess.run(['git', 'commit', '-m', 'DB changes'], check=True)

    # 変更をプッシュ
    push = subprocess.run(['git', 'push', 'origin', 'main'], check=True)

    # Gitのユーザー情報を設定
    subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)
    
    # もしプッシュにエラーが発生したらリモートリポジトリの最新の変更を取得してから再度プッシュ
    if push.returncode != 0:
        subprocess.run(['git', 'fetch', 'origin'], check=True)
        subprocess.run(['git', 'reset', '--hard', 'origin/main'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'DB changes'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)

    print("データベースの変更がGit上に反映され、リモートリポジトリにプッシュされました。")
except subprocess.CalledProcessError as e:
    print("エラーが発生しました：", e)
