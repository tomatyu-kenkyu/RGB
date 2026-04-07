import streamlit as st
from PIL import Image
import numpy as np
from collections import Counter

st.title("画像の色 Top10 抽出アプリ")

uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="アップロード画像", use_column_width=True)

    img_array = np.array(image)

    # 2次元 → 1次元（全ピクセル）
    pixels = img_array.reshape(-1, 3)

    st.write("解析中...")

    # RGBをタプルに変換してカウント
    pixel_list = [tuple(pixel) for pixel in pixels]
    counter = Counter(pixel_list)

    # 上位10件取得
    top10 = counter.most_common(10)

    st.subheader("出現頻度 Top10 色")

    for i, (color, count) in enumerate(top10, 1):
        r, g, b = color

        # 色表示用のHTML
        st.markdown(
            f"""
            **{i}位**  
            RGB: {color}  
            出現数: {count}  
            <div style="width:100px;height:30px;background-color:rgb({r},{g},{b});"></div>
            """,
            unsafe_allow_html=True
        )