import streamlit as st
from PIL import Image
import pytesseract

st.title("OCRアプリ（Tesseract）")

uploaded_file = st.file_uploader("画像をアップロード", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    text = pytesseract.image_to_string(image, lang="jpn")
    
    st.image(image, caption="アップロード画像")
    st.write("抽出結果👇")
    st.write(text)