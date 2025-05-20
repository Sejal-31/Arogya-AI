import streamlit as st
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import google.generativeai as gen_ai
from PIL import Image
import pandas as pd
import numpy as np
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

with st.sidebar:
    st.title("Feature Contents🌟")
    selected = option_menu(
        menu_title=None,  # required
        options=["🏠Home", "🩺Health Assist", "💪Fitness Assist"],
        default_index=0,
    )
    st.write('𝐒𝐞𝐥𝐞𝐜𝐭 𝐀𝐧𝐲 One Feature')

if selected == "🏠Home":
    st.title("🤖AI-Powered Personalized Health and Fitness Plans or Counsel🧑🏻‍⚕️💪")
    st.image(r"C:\Users\Dell\Pictures\FY_Project\156Z_2306.w017.n001.59A.p22.59.jpg")

if selected == "🩺Health Assist":
    st.title("𝙃𝙚𝙖𝙡𝙩𝙝 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝘼𝙨𝙨𝙞𝙨𝙩")

if selected == "💪Fitness Assist":
    st.title("𝙁𝙞𝙩𝙣𝙚𝙨𝙨 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝘼𝙨𝙨𝙞𝙨𝙩")

    GOOGLE_API_KEY = "AIzaSyAdvFMPLqVykZfKUU-chpnKQBQzKU9Avgc"
    genai.configure(api_key=GOOGLE_API_KEY)

    steps_count = st.number_input("Enter the number of steps:", min_value=0)
    distance_covered = st.number_input("Enter the distance covered (km):", min_value=0.0)
    calories_burned = st.number_input("Enter calories burned:", min_value=0)
    heart_rate = st.number_input("Enter heart rate (bpm):", min_value=0)
    sleep_duration = st.number_input("Enter sleep duration (hours):", min_value=0.0)

    # Button to submit inputs
    if st.button("Analyze"):
        input_data = (
            f"Steps: {steps_count} steps, "
            f"Distance: {distance_covered} km, "
            f"Calories: {calories_burned} kcal, "
            f"Heart Rate: {heart_rate} bpm, "
            f"Sleep Duration: {sleep_duration} hours."
        )

        # Generate response using the model
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_data)

        # Display the results
        st.subheader("Health Tracking Summary")
        st.write(input_data)
        st.subheader("Analysis:")
        st.write(response.text)


