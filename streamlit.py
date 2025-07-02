import streamlit as st
import pandas as pd
st.title("Smart Wireless Earphones for Enhanced Experience")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age:",min_value=0,max_value=120)
brand = st.text_input("Enter the earphone brand you're using")
experience = st.slider("Rate your experience (1 = Bad, 10 = Excellent):", 1, 10, 5)
battery = st.slider("Current battery level (%):", 0, 100, 50)
noise_cancellation = st.slider("Noise Cancellation (1-10)", 1, 10, 6)
mic_quality = st.slider("Mic Quality (1-10)", 1, 10, 6)

if st.button("submit"):
    st.write(f"Welcome {name}, age {int(age)}")
    st.write(f"Brand: {brand}")
    st.write(f"Experience Rating: {experience}/10")