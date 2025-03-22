import streamlit as st
import pickle
import os

# 设置 Streamlit 页面标题
st.title("SPBC Model Deployment")

# 方式 1：手动上传 `.pkl` 或 `.py` 文件
st.header("Upload your model file (rsf_model3.pkl) or Python script (.py)")
uploaded_file = st.file_uploader("Choose a file", type=["pkl", "py"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "pkl":
        try:
            # 读取上传的模型文件
            model = pickle.load(uploaded_file)
            st.success("Model loaded successfully!")

        except Exception as e:
            st.error(f"Failed to load the model: {e}")

    elif file_extension == "py":
        # 读取并显示 Python 代码内容
        st.success(f"Python script '{uploaded_file.name}' uploaded successfully!")
        script_content = uploaded_file.read().decode("utf-8")
        st.code(script_content, language="python")

else:
    st.warning("No file uploaded. Please upload a `.pkl` model file or a `.py` script.")
