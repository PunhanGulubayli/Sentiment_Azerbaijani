import streamlit as st
import cv2
import numpy as np
from fer import FER
import time

st.title("Face Sentiment Analysis (pseudo real-time)")

detector = FER(mtcnn=False)
img_placeholder = st.empty()
text_placeholder = st.empty()

while True:
    picture = st.camera_input("Take a selfie")
    if picture:
        # Streamlit image -> OpenCV
        file_bytes = np.asarray(bytearray(picture.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # FER analysis
        result = detector.detect_emotions(frame)
        if result:
            top_emotion, score = detector.top_emotion(frame)
            text_placeholder.text(f"Top emotion: {top_emotion} ({score:.2f})")
        else:
            text_placeholder.text("No face detected")

        # Show image
        img_placeholder.image(frame, channels="BGR")

    time.sleep(1)  # hər 1 saniyədən bir yenilənir
