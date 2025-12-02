import streamlit as st

st.title("사용자 입력 받는 페이지")

col1, _, col2 = st.columns(3)

with col1:
    nickname = st.text_input("닉네임 입력")
    age = st.text_input("나이 입력")
    country = st.selectbox("국적", ['한국', '중국', '일본', '미국', '외계'])
    hobby = st.radio("취미", ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질'])
    privacy = st.checkbox("개인정보 제공 동의")


with col2:
    if st.button("✅ 입력 완료~"):
        st.write(f"이름이 뭐야? {nickname}")
        st.write(f"몇 살이야? {age}")
        st.write(f"어디서 왔어? {country}")
        st.write(f"취미가 뭐야? {hobby}")
        st.write(f"개인정보 제공에 동의해? {privacy}")