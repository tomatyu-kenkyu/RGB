import streamlit as st
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR

st.title("OCRアプリ")

@st.cache_resource
def load_ocr():
    return PaddleOCR(use_angle_cls=True, lang='japanese')

ocr = load_ocr()

uploaded_file = st.file_uploader("画像アップロード", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_np = np.array(image)

    result = ocr.ocr(img_np)

    for line in result[0]:
        st.write(line[1][0])