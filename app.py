import face_recognition
import streamlit as st
from PIL import Image
import numpy as np

st.title("人脸识别 Demo")

uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    # 识别人脸位置
    face_locations = face_recognition.face_locations(img_array)
    st.write(f"检测到 {len(face_locations)} 张人脸")
    
    # 显示图片
    st.image(image, caption=f"检测到 {len(face_locations)} 张人脸", use_column_width=True)