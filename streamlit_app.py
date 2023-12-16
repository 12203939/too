# 必要なライブラリをインポート
import streamlit as st

# 画面タイトルの設定
st.title('三角形の面積計算アプリ')

# 三角形の底辺を入力するテキストボックス
base = st.text_input('底辺の長さを入力してください', '0')

# 三角形の高さを入力するテキストボックス
height = st.text_input('高さを入力してください', '0')

# 入力された値を浮動小数点数に変換
b = float(base)
h = float(height)

# 三角形の面積を計算
area = 0.5 * b * h

# 計算結果を表示
st.write('底辺：', b, '、高さ：', h, 'の三角形の面積は', area, 'です。')