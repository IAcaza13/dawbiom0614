import streamlit as st
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()

st.write(cars)

import polars as pl


df = pl.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})

st.write(df)

import altair as alt

chart = alt.Chart(df)

