import streamlit as st
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR

st.title("高精度OCR（無料版）")

@st.cache_resource
def load_ocr():
    return PaddleOCR(use_angle_cls=True, lang='japanese')

ocr = load_ocr()

uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    img = np.array(image)

    # 🔥 前処理なし（Cloud安定版）
    # 拡大だけやる
    img = np.repeat(np.repeat(img, 2, axis=0), 2, axis=1)

    result = ocr.ocr(img, cls=True)

    texts = []
    for line in result:
        for word in line:
            texts.append(word[1][0])

    st.subheader("抽出結果")
    st.write("\n".join(texts))