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
chart = alt.Chart(df).mark_point()


chart = alt.Chart(df).mark_point().encode(
    y='city'
)

chart = alt.Chart(df).mark_point().encode(
    x='precip',
    y='city'
)
chart = alt.Chart(df).mark_point().encode(
    alt.X('precip'),
    alt.Y('city')
)
chart = alt.Chart(df).mark_bar().encode(
    x='average(precip)',
    y='city'
)
mpg = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)')
)

hp = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Horsepower)')
)
hp3 = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Weight_in_lbs'),
    alt.Y('average(Miles_per_Gallon)')
)

chart = mpg | hp | hp3

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=["Name","Origin"]
).interactive()

st.altair_chart(chart)