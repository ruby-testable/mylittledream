import streamlit as st

# 가상 피드백 데이터
selected = st.feedback("stars")

if selected is not None:
    st.write(f"별점 {selected + 1}을 선택하셨습니다.")