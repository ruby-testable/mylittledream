import streamlit as st

# 가상 폼 생성
with st.form("my_form"):
    name = st.text_input("이름")
    age = st.number_input("나이", min_value=0)
    submit = st.form_submit_button("제출")

if submit:
    st.write(f"이름: {name}, 나이: {age}")