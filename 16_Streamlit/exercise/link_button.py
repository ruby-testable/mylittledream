import streamlit as st

# 셀렉트 슬라이더 생성
size = st.select_slider("사이즈를 선택하세요:", options=["S", "M", "L", "XL"])

st.write(f"선택된 사이즈: {size}")