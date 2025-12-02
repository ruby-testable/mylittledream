import streamlit as st

st.title("오늘은 화🔥🔥🔥요일")
st.header("오늘은 Streamlit 배우는 두번째 날")
st.subheader("Streamlit으로 나만의 데모 페이지를 만들어보자")

today_page = st.text_input("오늘 내가 정할 페이지의 이름은???!!?!!?")

st.write(today_page)
if st.button(f"{today_page}에 접속해보기"):
    st.write(f"{today_page}에 접속 중임!!!!")