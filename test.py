import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import pandas as pd
import seaborn as sns

from graph import Graph

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

is_graph = st.checkbox('年齢をグラフ化する')
if is_graph:
    max_age = st.slider('年齢の上限', 0, 5, 3)
    age_ticks = range(max_age + 1)
    
    park_list = df["公園"].to_list()
    select_park = st.multiselect('表示する公園名を選択', park_list, park_list[0])
    df = df[df['公園'].isin(select_park)]
    
    # fig, ax = plt.subplots()
    # ax.bar(df["公園"], df["年齢"])
    # ax.set_ylim([0, max_age])
    # ax.set_yticks(age_ticks)
    # ax.set_title("公園と年齢")
    # ax.set_xlabel("公園")
    # ax.set_ylabel("年齢")
    # st.pyplot(fig)

    graph_obj = Graph(y_min=0, y_max=max_age, g_title="公園と年齢", x_label="公園", y_label="年齢", y_ticks=age_ticks)
    graph_obj.plot_bar(df["公園"], df["年齢"], st)

