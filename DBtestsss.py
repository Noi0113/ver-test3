import sqlite3
import subprocess
import os
import streamlit as st

# カレントディレクトリをリポジトリのディレクトリに変更
#os.chdir('ver-test3')

st.title('DBテストsubprocessに賭けた版！！!')

# ユーザーからの入力を収集
user_input = st.text_input("何か入力してください")

if st.button("送信"):
    # データをデータベースに保存
    conn = sqlite3.connect('test-monketsu3.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_inputs (input TEXT)")
    c.execute("INSERT INTO user_inputs VALUES (?)", (user_input,))
    conn.commit()
    conn.close()

    # データベースの内容を表示
    st.write(f"あなたが入力したテキスト: {user_input}")

    try:
        
        # Gitのユーザー情報を設定
        subprocess.check_call(['git', 'config', '--global', 'user.email', 's2110524@u.tsukuba.ac.jp'])
        subprocess.check_call(['git', 'config', '--global', 'user.name', 'KNo0113'])


        # ①現在のリポジトリが存在するリポジトリに移動
        current_directory = os.getcwd()

        # ②もしリポジトリが存在していなければそのリポジトリのクローンをつくる
        if not os.path.exists('.git'):
            subprocess.run(['git', 'clone', 'https://github.com/Noi0113/ver-test3.git'])
            current_directory = os.getcwd()

        # ③DBの変更を追加する
        subprocess.run(['git', 'add', '.'])

        # ④変更をプッシュ
        push = subprocess.run(['git', 'push', 'origin', 'main'])

        # ⑤もしpushにエラーがでたら git fetch originを実行しリモートリポジトリの最新の変更を取得
        if push.returncode != 0:
            subprocess.run(['git', 'fetch', 'origin'])

        # ⑥ git reset --hard origin/mainを実行しローカルブランチをリモートブランチの最新の状態にリセットする
            subprocess.run(['git', 'reset', '--hard', 'origin/main'])

        # ⑦DBの変更を追加する
            subprocess.run(['git', 'add', '.'])

        # ⑧変更をコミットする
            subprocess.run(['git', 'commit', '-m', 'DB changes'])

        # ⑨変更をプッシュする
            subprocess.run(['git', 'push', 'origin', 'main'])

            print("データベースの変更がGit上に反映され、リモートリポジトリにプッシュされました。")
    except subprocess.CalledProcessError as e:
        print("エラーが発生しました：", e)
