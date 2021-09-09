import cv2
import mediapipe
import time

capture = cv2.VideoCapture(0)

mediapipeHands = mediapipe.solutions.hands
hands = mediapipeHands.Hands()

mediapipeDraw = mediapipe.solutions.drawing_utils

while True:
    success, img = capture.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            mediapipeDraw.draw_landmarks(img, handLandmarks, mediapipeHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
