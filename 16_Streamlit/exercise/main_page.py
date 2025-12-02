import streamlit as st

today = st.text_input("오늘 내가 만들어보고 싶은 사이트는?!!??!?!??!")

if st.button(f"{today} 접속 하기"):
    st.write(f"{today} 접속 중읾...아,,,")