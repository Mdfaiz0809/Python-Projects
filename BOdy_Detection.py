import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()
cap = cv2.VideoCapture("C:\\Users\\MD WASIM SHAIKH\\OneDrive\\Desktop\\Python projects\\2.mp4")

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (600, 400))

    results = pose.process(img)
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((0, 0, 0), 2, 2),
                           mp_draw.DrawingSpec((0, 0, 0), 2, 2))
    cv2.imshow("Pose Estimaton", img)
    h, w, c = img.shape
    opImg = np.zeros([h, w, c])
    opImg.fill(255)
    mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                           mp_draw.DrawingSpec((0, 0, 255), 2, 2),
                           mp_draw.DrawingSpec((0, 255, 0), 2, 2))
    cv2.imshow("Extracted pose", opImg)

    print(results.pose_landmarks)

    cv2.waitKey(1)
