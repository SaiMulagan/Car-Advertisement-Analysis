import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Streamlit App
st.title('Exploratory Data Analysis (EDA) for US Vehicle Listings')
st.write("""
This application provides insights into the distribution of various attributes of vehicles listed in the US.
Currently, we're exploring the vehicle's price distribution and the relationship between model year and price.
""")

# Price Distribution Histogram
fig_price = px.histogram(df, x="price", title="Price Distribution")
fig_price.update_layout(yaxis_title="Number of Vehicles")
st.plotly_chart(fig_price)

# Model Year vs Price Scatter Plot
fig_scatter = px.scatter(df, x="model_year", y="price", title="Model Year vs Price")
st.plotly_chart(fig_scatter)

# Filters
min_year, max_year = int(df["model_year"].min()), int(df["model_year"].max())
year_range = st.slider("Filter by Model Year:", min_year, max_year, (min_year, max_year))
filtered_df = df[(df["model_year"] >= year_range[0]) & (df["model_year"] <= year_range[1])]

# Display filtered scatter plot if range is changed
if year_range != (min_year, max_year):
    st.write(f"Displaying data for model years: {year_range[0]} - {year_range[1]}")
    fig_filtered_scatter = px.scatter(filtered_df, x="model_year", y="price", title="Model Year vs Price (Filtered)")
    st.plotly_chart(fig_filtered_scatter)

# Checkboxes to show additional elements
if st.checkbox('Show Data Table'):
    st.write(filtered_df)
