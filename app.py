# app.py
import streamlit as st
from tw_sentiment import analyze_text  # yalnız text sentiment

st.set_page_config(page_title="Azerbaijani Text Sentiment", layout="centered")
st.title("Azerbaijani Text Sentiment Analysis")

# Input text
user_input = st.text_area("Metn daxil edin:")

if st.button("Analiz et"):
    if user_input.strip() != "":
        sentiment, score = analyze_text(user_input)
        st.write(f"Sentiment: {sentiment}")
        # float çevrilməsi üçün try/except
        try:
            st.write(f"Confidence: {float(score):.2f}")
        except (ValueError, TypeError):
            st.write(f"Confidence: {score}")
    else:
        st.warning("Zəhmət olmasa metn daxil edin.")


