import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
# lower_yello = np.array([22, 93, 0])
# upper_yello = np.array([45, 255, 255])
# lower_black = np.array([0, 0, 0])
# upper_black  = np.array([50, 50, 100])
lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
prev_y = 0
prev_x = 0

while True:
    ret, frame = cap.read()
    # gray test
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('frame', gray)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)  # print all detection

    for c in contours:
        area = cv2.contourArea(c)
        if area > 300:
            cv2.drawContours(frame, c, -1, (0, 255, 0), 2)  # print bigger detection
            x, y, w, h = cv2.boundingRect(c)  # find rectangle coordinate
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw rectange
            pyautogui.press('down') if y < prev_y else pyautogui.press('up')
            pyautogui.press('left') if x < prev_x else pyautogui.press('right')
            prev_y = y
            prev_x = x

    cv2.imshow('frame', frame)
    cv2.imshow('frame_new', mask)

    if cv2.waitKey(10) == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()

