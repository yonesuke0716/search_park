import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

sns.set(font="IPAexGothic")

st.markdown(" ## 公園検索")
df = pd.read_excel("test.xlsx", engine="openpyxl")
machi = df["市町村"].unique().tolist()
toshi = df["年齢"].unique().tolist()
m_select = st.sidebar.selectbox("市町村を選択してください", machi)
t_select = st.sidebar.selectbox("年齢を選択してください", toshi)
result_df = df[(df["市町村"] == m_select) & (df["年齢"] == t_select)]
if len(result_df) == 0:
    st.write("一致する結果はありません")
else:
    st.write("一致した場所： ")
    for i in range(len(result_df)):
        st.write(result_df["公園"].values[i])
        url = result_df["URL"].values[i]
        link = f"[{url}]({url})"
        st.markdown(link, unsafe_allow_html=True)

fig, ax = plt.subplots()
ax.bar(df["公園"], df["年齢"])
ax.set_ylim([0, 3])
ax.set_yticks([0, 1, 2, 3])
ax.set_title("公園と年齢")
ax.set_xlabel("公園")
ax.set_ylabel("年齢")
st.pyplot(fig)
