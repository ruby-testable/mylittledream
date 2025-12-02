import streamlit as st
import pandas as pd
import numpy as np

# 가상 데이터 생성: 2025년 분기별 매출 및 예상 성장률
data = pd.DataFrame({
    '분기': ['Q1', 'Q2', 'Q3', 'Q4'],
    '매출액': [15000, 18000, 22000, 25000],
    '예상 성장률 (%)': [5, 7, 10, 12]
})

# 매출액 영역 차트 생성
st.subheader("2025년 분기별 매출 현황")
st.area_chart(data.set_index('분기')[['매출액']])

# 성장률 정보도 텍스트로 제공
st.write("2025년 분기별 예상 성장률:")
st.dataframe(data[['분기', '예상 성장률 (%)']])