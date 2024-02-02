import subprocess
import sqlite3
import streamlit as st
import os

st.title('確認!!')
# StreamlitのWebサイトで入力された情報を取得
input_data = st.text_input('Enter your data')

# リポジトリのディレクトリが存在するか確認
if not os.path.exists('ver-test3'):
    # リポジトリをクローン
    subprocess.run(['git', 'clone', 'https://github.com/Noi0113/ver-test3.git'], check=True)
else:
    # ローカルリポジトリに移動
    os.chdir('ver-test3')
    # リポジトリを更新
    subprocess.run(['git', 'pull'], check=True)

# データベースファイルに書き込み
conn = sqlite3.connect('test-monketsu3.db')
c = conn.cursor()
# ここでは例としてテーブル名を 'TABLE_NAME'、カラム名を 'COLUMN_NAME' としています。
# 実際には適切なテーブル名とカラム名を指定してください。
c.execute("INSERT INTO TestTable3 (univ) VALUES (?)", (input_data,))
conn.commit()
conn.close()

# 変更をステージング
subprocess.run(['git', 'add', '.'], check=True)

#何者か
subprocess.run(["git", "config", "--global", "user.name", "Noi0113"], check=True)
subprocess.run(["git", "config", "--global", "user.email", "s2110524@u.tsukuba.ac.jp"], check=True)

# コミット
subprocess.run(['git', 'commit', '-m', 'Update database file'], check=True)

# リモートリポジトリにpush
subprocess.run(['git', 'push','origin','main'], check=True)
