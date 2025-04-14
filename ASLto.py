import cv2
import os 
import mediapipe as mp
import numpy as np
import joblib
import time
import math as math
from cmu_graphics import *

def translateFromASL(img,model,hands,mp_draw):
    def normalize_landmarks(landmarks):
        base_x, base_y, base_z = landmarks[0:3]
        norm = []
        for i in range(0, len(landmarks), 3):
            norm.append(landmarks[i] - base_x)
            norm.append(landmarks[i+1] - base_y)
            norm.append(landmarks[i+2] - base_z)
        return norm


    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    prediction = ''


    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

            # Get landmark positions as a flat list
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])  # flatten into a vector

            norm = normalize_landmarks(landmarks)
            prediction = model.predict([norm])[0]

    if prediction:
        cv2.putText(img, f'Prediction: {prediction}', (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    return prediction, img
