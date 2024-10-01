import streamlit as st
from functions import *
import numpy as np

st.set_page_config(layout="wide")

# Use the full path for the image
st.image('images/home_image.png', width=1120)

# Show the input fields horizontally on the home page
st.title("Check your flight!")
st.write("Input your flight details below to predict delays:")

# Display the toolbar (flight input fields)
show_toolbar()

# Button to display previous saved searches
if st.button('Show Previous Searches'):
    saved_predictions = load_saved_predictions()

    if not saved_predictions.empty:
        st.write("Previous Searches and Predictions:")
        st.dataframe(saved_predictions)
    else:
        st.write("No previous searches found.")

# Text for Tableau
st.title("Looking for your next trip?")
st.write("Check the available airlines and their performance for your destination")

# Image of dashboard
st.image('images/tableau_dashboard.png', width=1120)

st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <a href='https://public.tableau.com/views/Departures_Dashboard/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link' target='_blank' style='font-size:18px;'>
            Use This Dashboard
        </a>
    </div>
    """, unsafe_allow_html=True)
