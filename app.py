import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

st.header('Car Advertisement Data')

if st.checkbox('Show Price Histogram'):
    fig = px.histogram(df, x="price", title="Price Distribution")
    st.plotly_chart(fig)

if st.checkbox('Show Model Year vs Price Scatter Plot'):
    fig_scatter = px.scatter(df, x="model_year", y="price", title="Model Year vs Price")
    st.plotly_chart(fig_scatter)

