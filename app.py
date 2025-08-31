# app.py
import streamlit as st
import cv2
import numpy as np
from tw_sentiment import analyze_text
from sentiment_face import analyze_face
from streamlit_autorefresh import st_autorefresh

st.title("Sentiment Analysis App")

# İstifadəçi seçim
option = st.radio("Choose input type:", ["Text", "Face"])

if option == "Text":
    user_input = st.text_area("Enter your text:")
    if st.button("Analyze Text"):
        if user_input.strip() != "":
            translated_text, result = analyze_text(user_input)
            st.write("🔄 Translated Text:", translated_text)
            st.write("📊 Sentiment Results:")
            for label, score in result.items():
                st.write(f"{label}: {score:.4f}")
        else:
            st.warning("Please enter some text!")

elif option == "Face":
    st.write("Pseudo Real-time Face Sentiment")

    # Placeholder-lar
    img_placeholder = st.empty()
    text_placeholder = st.empty()

    # Auto-refresh hər 1 saniyə
    count = st_autorefresh(interval=1000, limit=None, key="facedetect")

    picture = st.camera_input("Take a selfie")
    if picture:
        # Streamlit image -> OpenCV
        file_bytes = np.asarray(bytearray(picture.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # FER analizi
        top_emotion, score = analyze_face(frame)
        if top_emotion:
            text_placeholder.text(f"Top emotion: {top_emotion} ({score:.2f})")
        else:
            text_placeholder.text("No face detected")

        # Şəkli göstər
        img_placeholder.image(frame, channels="BGR")
