import cv2
import os 
import mediapipe as mp
import numpy as np
import joblib
import time
import math as math
from cmu_graphics import *

model = joblib.load('asl_knn_model.pkl')

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def normalize_landmarks(landmarks):
    base_x, base_y, base_z = landmarks[0:3]
    norm = []
    for i in range(0, len(landmarks), 3):
        norm.append(landmarks[i] - base_x)
        norm.append(landmarks[i+1] - base_y)
        norm.append(landmarks[i+2] - base_z)
    return norm

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    prediction = ''


    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions as a flat list
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])  # flatten into a vector

            norm = normalize_landmarks(landmarks)
            prediction = model.predict([norm])[0]

    if prediction:
        cv2.putText(frame, f'Prediction: {prediction}', (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Tracking", img)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

def translateFromASL(app,frame):
    pass


                
if __name__ == "__main__":
    main()

cmu_graphics.run()