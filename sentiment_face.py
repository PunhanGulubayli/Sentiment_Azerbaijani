# sentiment_face.py
from fer import FER

# FER detector obyektini yaradın (bir dəfə)
detector = FER(mtcnn=False)

def analyze_face(frame):
    """
    frame: OpenCV image (numpy array)
    return: top emotion + score
    """
    result = detector.detect_emotions(frame)
    if result:
        top_emotion, score = detector.top_emotion(frame)
        return top_emotion, score
    else:
        return None, None

