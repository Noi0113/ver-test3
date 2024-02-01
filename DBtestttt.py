import streamlit as st
import sqlite3
import os
import subprocess

# データベースに接続
conn = sqlite3.connect('test-monketsu3.db')
c = conn.cursor()

# Streamlitでユーザー入力を取得
user_input = st.text_input("Please enter your data")

# ユーザーが何かを入力した場合
if user_input:
    c.execute("SELECT * FROM TestTable3")
    rows = c.fetchall()
    for row in rows:
        st.write(row)

    # SQLクエリを作成（ここではテーブル名を 'your_table' と仮定）
    query = f"INSERT INTO TestTable3 (univ) VALUES ('{user_input}')"

    # クエリを実行
    c.execute(query)

    # 変更をコミット
    conn.commit()

    # データベースファイルをGitに追加
    subprocess.run(["git", "add", "test-monketsu3.db"])

    # 変更をコミット
    subprocess.run(["git", "commit", "-m", "Update database file"])

    # 変更をGitHubにプッシュ
    subprocess.run(["git", "push", "origin", "master"])
