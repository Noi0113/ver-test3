import subprocess
import sqlite3
import streamlit as st
import os

st.title('確認!')
# StreamlitのWebサイトで入力された情報を取得
input_data = st.text_input('Enter your data')

# リポジトリのディレクトリが存在するか確認
if not os.path.exists('ver-test3'):
    # リポジトリをクローン
    subprocess.check_call(['git', 'clone', 'https://github.com/Noi0113/ver-test3.git'])
else:
    # ローカルリポジトリに移動
    os.chdir('ver-test3')
    # リポジトリを更新
    subprocess.check_call(['git', 'pull'])

# データベースファイルに書き込み
conn = sqlite3.connect('test-monketsu3.db')
c = conn.cursor()
# ここでは例としてテーブル名を 'TABLE_NAME'、カラム名を 'COLUMN_NAME' としています。
# 実際には適切なテーブル名とカラム名を指定してください。
c.execute("INSERT INTO TestTable3 (univ) VALUES (?)", (input_data,))
conn.commit()
conn.close()

# 変更をステージング
subprocess.check_call(['git', 'add', '.'])

# 何者か
subprocess.check_call(["git", "config", "--global", "user.name", "Noi0113"])
subprocess.check_call(["git", "config", "--global", "user.email", "s2110524@u.tsukuba.ac.jp"])

# コミット
subprocess.check_call(['git', 'commit', '-m', 'Update database file'])

# リモートリポジトリにpush
subprocess.check_call(['git', 'push','origin','main'])
