import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
lower_yello = np.array([22, 93, 0])
upper_yello = np.array([45, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    # gray test
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yello, upper_yello)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2) #print all detection

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            cv2.drawContours(frame, c, -1, (0, 255, 0), 2) #print bigger detection
            x, y, w, h = cv2.boundingRect(c) # find rectangle coordinate
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #draw rectange
            if y < prev_y:
                pyautogui.press('space')

            prev_y = y

    cv2.imshow('frame', frame)
    cv2.imshow('frame_new', mask)

    if cv2.waitKey(10) == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()


