# app.py
import streamlit as st
from tw_sentiment import analyze_text  # yalnız text sentiment

st.title("Azerbaijani Text Sentiment Analysis")

# Input text
user_input = st.text_area("Metn daxil edin:")

if st.button("Analiz et"):
    if user_input.strip() != "":
        sentiment, score = analyze_text(user_input)
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Confidence: {score:.2f}")
    else:
        st.warning("Zəhmət olmasa metn daxil edin.")

