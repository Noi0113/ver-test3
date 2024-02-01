import sqlite3
import subprocess
import os
import streamlit as st

#os.chdir('ver-test3')
st.title('DBテストsubprocessに賭けた版!！')
# ユーザーからの入力を収集
user_input = st.text_input("何か入力してください")

if st.button("送信"):
    # データをデータベースに保存
    conn = sqlite3.connect('test-monketsu3.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_inputs (input TEXT)")
    c.execute("INSERT INTO user_inputs VALUES (?)", (user_input,))
    conn.commit()

    # データベースの内容を表示
    c.execute("SELECT * FROM user_inputs")
    rows = c.fetchall()
    for row in rows:
        st.write(row)

    conn.close()
    st.write(f"あなたが入力したテキスト: {user_input}")

    # Gitコマンドを実行
    #try:
    #    subprocess.check_call(['git', 'config', '--global', 'user.email', 's2110524@u.tsukuba.ac.jp'])
    #    subprocess.check_call(['git', 'config', '--global', 'user.name', 'KNo0113'])
     #   subprocess.check_call(['git', 'add', '--all'])
     #   subprocess.check_call(['git', 'commit', '-m', 'Update database'])
     #   subprocess.check_call(['git', 'reset', '--hard', 'origin/main'])
      #  subprocess.check_call(['git', 'add', 'test-monketsu3.db'])
      #  subprocess.check_call(['git', 'fetch', 'origin'])
       # subprocess.check_call(['git', 'commit', '-m', 'Add SQLite database'])
        #subprocess.check_call(['git', 'push'])
        #st.write("データベースがGitHubリポジトリにプッシュされました。")
    #except subprocess.CalledProcessError as e:
     #   st.write("エラーが発生しました：", e)


    #クローン作製

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
        #subprocess.check_call(['git', 'add', 'test-monketsu3.db'])

        # リモートリポジトリの最新情報を取得
        subprocess.check_call(['git', 'fetch', 'origin'])

        # リモートリポジトリから最新の変更を取得
        subprocess.check_call(['git', 'pull', 'origin', 'main'])

        # 変更をコミット
        subprocess.check_call(['git', 'commit', '-m', 'Add SQLite database'])

        # リモートリポジトリにプッシュ（SSH接続）
        subprocess.check_call(['git', 'push', 'git@github.com:Noi0113/ver-test3.git', 'main'])

        print("データベースの変更がGit上に反映され、リモートリポジトリにプッシュされました。")
    except subprocess.CalledProcessError as e:
        print("エラーが発生しました：", e)
