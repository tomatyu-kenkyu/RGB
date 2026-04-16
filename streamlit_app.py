import streamlit as st
from PIL import Image
import easyocr
import numpy as np

st.title("画像から文字抽出（EasyOCR）")

# アップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="アップロード画像", use_column_width=True)

    # OCR実行
    with st.spinner("文字認識中..."):
        reader = easyocr.Reader(['ja', 'en'])  # 日本語＋英語
        result = reader.readtext(np.array(image))

    # 結果表示
    st.subheader("抽出結果（テキストのみ）")
    text_only = [res[1] for res in result]
    st.write("\n".join(text_only))

    # 詳細表示（位置・信頼度）
    st.subheader("詳細（座標・信頼度）")
    for bbox, text, prob in result:
        st.write(f"文字: {text} / 信頼度: {prob:.2f}")