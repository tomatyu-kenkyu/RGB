import streamlit as st
from PIL import Image
import numpy as np

st.title("画像のRGB値取得アプリ")

# 画像アップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 画像読み込み
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(image, caption="アップロード画像", use_column_width=True)

    st.write("画像サイズ:", img_array.shape)

    # 座標入力
    st.subheader("座標を指定してRGB取得")
    x = st.number_input("X座標（横）", min_value=0, max_value=img_array.shape[1]-1, value=0)
    y = st.number_input("Y座標（縦）", min_value=0, max_value=img_array.shape[0]-1, value=0)

    # RGB取得
    rgb = img_array[y, x]

    st.write(f"座標 ({x}, {y}) のRGB値:")
    st.write(f"R: {rgb[0]}, G: {rgb[1]}, B: {rgb[2]}")

    # 平均RGB
    st.subheader("画像全体の平均RGB")
    avg_rgb = img_array.mean(axis=(0, 1))
    st.write(f"R: {avg_rgb[0]:.2f}, G: {avg_rgb[1]:.2f}, B: {avg_rgb[2]:.2f}")