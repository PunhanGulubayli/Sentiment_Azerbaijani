# app.py
import streamlit as st
from tw_sentiment import analyze_text  # sənin verdiyin funksiyanı ehtiva edir

st.set_page_config(page_title="Azerbaijani Text Sentiment", layout="centered")
st.title("Azerbaijani Text Sentiment Analysis")

user_input = st.text_area("Metn daxil edin:")

if st.button("Analiz et"):
    if user_input.strip() != "":
        translated_text, scores = analyze_text(user_input)

        st.write(f"Translated text: {translated_text}")

        # ən yüksək skorlu label
        sentiment = max(scores, key=scores.get)
        st.write(f"Sentiment: {sentiment}")

        st.write("Confidence scores:")
        for label, score in scores.items():
            st.write(f"{label}: {score:.5f}")  # 5 rəqəmli kəsr hissəsi
    else:
        st.warning("Zəhmət olmasa metn daxil edin.")

