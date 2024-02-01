import streamlit as st
import sqlite3
import subprocess

st.title('できたかもしれない??')
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
    #subprocess.run(["git", "add", "test-monketsu3.db"])

    # 変更をコミット
    #subprocess.run(["git", "commit", "-m", "Update database file"])

    # 変更をGitHubにプッシュ
    #subprocess.run(["git", "push", "origin", "main"])
    #result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    #st.write(result.stdout)
    #st.write(result.stderr)
# Gitコマンドを実行
    try:
    # Gitのユーザー情報を設定
        subprocess.check_call(['git', 'config', '--global', 'user.email', 's2110524@u.tsukuba.ac.jp'])
        subprocess.check_call(['git', 'config', '--global', 'user.name', 'KNo0113'])

        # 変更をステージング
        subprocess.check_call(['git', 'add', '--all'])

        # コミット
        subprocess.check_call(['git', 'commit', '-m', 'Update database'])

        # リモートのmainブランチを最新状態にリセット
        subprocess.check_call(['git', 'reset', '--hard', 'origin/main'])

        # 変更を再度ステージング
        subprocess.check_call(['git', 'add', 'test-monketsu3.db'])
    
        #リモートリポジトリの最新情報を取得
        subprocess.check_call(['git', 'fetch', 'origin'])

        # 変更をコミット
        subprocess.check_call(['git', 'commit', '-m', 'Add SQLite database'])

        # リモートリポジトリにプッシュ
        subprocess.check_call(['git', 'push'])

        print("データベースの変更がGit上に反映され、リモートリポジトリにプッシュされました。")
    except subprocess.CalledProcessError as e:
        print("エラーが発生しました：", e)
