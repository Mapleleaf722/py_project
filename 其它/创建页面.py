import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("./塞尔达.xlsx", type=["xlsx"])
# st.text("测试xxxx")
if uploaded_file is None:
    st.stop()
df = pd.read_excel(uploaded_file, None)
names = list(df.keys())
sheet_selects = st.multiselect('工作表', names, [])
