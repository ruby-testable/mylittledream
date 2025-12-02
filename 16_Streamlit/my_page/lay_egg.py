import streamlit as st
from streamlit_autorefresh import st_autorefresh

if "interval" not in st.session_state:
    st.session_state.interval = 3500

st_autorefresh(interval=st.session_state.interval, limit=None, key="auto")

if "count" not in st.session_state:
    st.session_state.count = 0
    st.session_state.money = 0

if "image_state" not in st.session_state:
    st.session_state.image_state = "none"

if "title_state" not in st.session_state:
    st.session_state.title_state = "none"

st.session_state.count += 1
st.session_state.money += 100

title_container = st.empty()
image_container = st.empty()
st.write("생산한 달걀:", st.session_state.count)

if st.session_state.money >= 0:
    st.write(f"💰 현재 자금: {st.session_state.money}원")

if st.session_state.money < 0:
    st.write(f"💸 현재 빚: {st.session_state.money}원")

if "button_disabled1" not in st.session_state:
    st.session_state.button_disabled1 = False
if "button_disabled2" not in st.session_state:
    st.session_state.button_disabled2 = False
if "button_disabled3" not in st.session_state:
    st.session_state.button_disabled3 = False
if "button_disabled4" not in st.session_state:
    st.session_state.button_disabled4 = False

def on_button_click1():
    st.session_state.button_disabled1 = True
    st.session_state.money -= 1000
    st.session_state.interval = 2500
    st.session_state.image_state = "chicken1"
    st.success("1000원을 내고 닭을 키우기 시작했어요!")

def on_button_click2():
    st.session_state.button_disabled2 = True
    st.session_state.money -= 3000
    st.session_state.interval = 2000
    st.session_state.image_state = "chicken2"
    st.success("3000원을 내고 닭을 영입했어요!")

def on_button_click3():
    st.session_state.button_disabled3 = True
    st.session_state.money -= 10000
    st.session_state.interval = 1500
    st.session_state.image_state = "chicken3"
    st.success("10000원을 내고 닭에게 목도리를 둘러줬어요!")

def on_button_click4():
    st.session_state.button_disabled4 = True
    st.session_state.money -= 20000
    st.session_state.interval = 10000000
    st.session_state.image_state = "chicken4"
    st.session_state.title_state = "chicken"
    st.success("20000원을 내고 치킨을 얻었어요!")

st.button(
    "1000원을 내고 닭을 키워보자!",
    on_click=on_button_click1,
    disabled=st.session_state.button_disabled1
)

st.button(
    "3000원을 내고 닭을 영입하자!",
    on_click=on_button_click2,
    disabled=st.session_state.button_disabled2
)

st.button(
    "10000원을 내고 닭에게 목도리를 둘러주자!",
    on_click=on_button_click3,
    disabled=st.session_state.button_disabled3
)

if st.session_state.money >= 20000:
    st.button(
    "20000원을 내면...",
    on_click=on_button_click4,
    disabled=st.session_state.button_disabled4
)
    
if st.button("돈복사버튼"):
    st.session_state.money += 10000

if st.session_state.image_state == "chicken1":
    image_container.image("a.png")
elif st.session_state.image_state == "chicken2":
    image_container.image("b.png")
elif st.session_state.image_state == "chicken3":
    image_container.image("c.png")
elif st.session_state.image_state == "chicken4":
    image_container.image("d.png")
else:
    image_container.image("0.png")

if st.session_state.title_state == "chicken":
    title_container.title("치킨 사먹기 시뮬레이터")
else:
    title_container.title("달걀 농장 시뮬레이터")