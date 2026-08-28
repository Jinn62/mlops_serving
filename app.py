import streamlit as st
import requests

API_URL = "http://34.45.237.104/predict"

st.title("붓꽃 분류기 (Iris Classifier)")

s_l = st.slider("꽃받침 길이", 0.0, 8.0, 5.0)
s_w = st.slider("꽃받침 너비", 0.0, 4.5, 3.0)
p_l = st.slider("꽃잎 길이", 0.0, 7.0, 1.5)
p_w = st.slider("꽃잎 너비", 0.0, 2.5, 0.2)

if st.button("예측하기"):
    try:
        response = requests.post(
            API_URL,
            json={"data": [s_l, s_w, p_l, p_w]},
            timeout=5,
        )
        response.raise_for_status()
        st.success(f"예측된 클래스 번호: {response.json()['class_index']}")
    except requests.exceptions.RequestException as error:
        st.error(f"API 서버에 연결할 수 없습니다: {error}")