from email.policy import default

import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")


place = st.text_input("Place: ")

days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [item['main']['temp'] for item in filtered_data]
        dates = [item['dt_txt'] for item in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y":"Temperature (c)"})
        st.plotly_chart(figure)

    elif option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [item['weather'][0]['main'] for item in filtered_data]
        images_path = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(images_path, width=115)