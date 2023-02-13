import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.set_page_config(page_title="Faris' Webpage", page_icon=":tada:", layout="wide")

# ----HEADER SECTION ----
st.subheader("Hi, I am Faris")
st.title("A really bored guy......")
st.write("Hoaaahmmmm")

# ---- table with write() function ----
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

# ---- table with dataframe() function formatted ----
st.dataframe(dataframe.style.highlight_max(axis=0)) # max value in each column are highlighted

# ---- table with table() function ----
st.table(dataframe)


# ---- chart ----

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# ---- map ----
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)