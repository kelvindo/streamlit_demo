import streamlit as st
import pandas as pd
import altair as alt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/uber-raw-data-sep14.csv.gz', compression='gzip')
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])  # Convert to datetime format

    return data

data = load_data()

# Add a title and description
st.title("Uber pickups in NYC")
st.markdown("""
    This app displays the number of Uber pickups in each hour of the day for a given day.
    Use the slider to select a specific hour and see how the number of pickups changes throughout the day.
""")

# Create a slider for selecting the hour
hour = st.slider("Hour of the day", 0, 23)

# Filter the data based on the hour
filtered_data = data[data["Date/Time"].dt.hour == hour]

# Display the number of pickups
st.write("Number of pickups:", len(filtered_data))

# Create a histogram of the pickup locations using Altair
st.write("Map of all pickups at %s:00" % hour)
hist = alt.Chart(filtered_data).mark_circle(size=3).encode(
    alt.X('Lon:Q', scale=alt.Scale(domain=(-74.2, -73.7))),
    alt.Y('Lat:Q', scale=alt.Scale(domain=(40.6, 40.9))),
    color=alt.value('steelblue')
).properties(
    width=800,
    height=500
).interactive()

st.write(hist)
