import streamlit as st
from PIL import Image
import numpy as np
import cv2
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

    # 🔥 前処理（超重要）
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)

    # 拡大（小さい文字対策）
    thresh = cv2.resize(thresh, None, fx=2, fy=2)

    # OCR
    result = ocr.ocr(thresh, cls=True)

    # テキスト抽出
    texts = []
    for line in result:
        for word in line:
            texts.append(word[1][0])

    st.subheader("抽出結果")
    st.write("\n".join(texts))