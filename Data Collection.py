import cv2
import mediapipe as mp
import numpy as np
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
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

with open('asl_data.csv', 'a', newline='') as f:
    writer = csv.writer(f)

    while True:
        ret, frame = cap.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                
                norm = normalize_landmarks(landmarks)

                key = cv2.waitKey(1)
                if 97 <= key <= 122 or key == 59:  # A-Z
                    label = chr(key)
                    writer.writerow(norm + [label])
                    print(f"Saved: {label}")

        cv2.imshow("Collect ASL Data - Press A-Z to Label", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
