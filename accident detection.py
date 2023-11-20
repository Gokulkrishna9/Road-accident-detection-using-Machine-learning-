import cv2
import time
from tkinter import *
from tkinter import messagebox
import pygame
import smtplib

pygame.init()

pygame.mixer.music.load("alarm.wav")
# Capturing Video
cap = cv2.VideoCapture("assets/i.mp4")

if not cap.isOpened():
    print("Initialising the capture...")
    cap.open("assets/test_35.mp4")
    print("Done.")

# Subtracting the background
subtractor = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=20)

# Text setting up
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = (40, 50)

# fontScale
fontScale = 0.8

# Blue color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2

res = 1

arcount = 0

count = -1

while True:
    # Reading the frame
    res, frame = cap.read()

    if res == True:
        # Applying the mask
        mask = subtractor.apply(frame)

    # finding the contours
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Flag for accident detection
        flag = 0

        for cnts in contours:
            (x, y, w, h) = cv2.boundingRect(cnts)

            if w * h > 1000:
                

        # If area of rectangle more than a threshold detect accident
            if w * h > 10000:
                area = w * h
            # Countint the number of frames for which the condition persists to refine the accident detection case
                arcount += 1
            # print(arcount)
            if arcount > 35:
                flag = 1

        if flag == 1:
            # If accident detected print Accident on the screen
            frame = cv2.putText(frame, "Accident Detected ", org, font,
                                fontScale, color, thickness, cv2.LINE_AA, False)
            try:
                pygame.mixer.music.play()
                s = smtplib.SMTP('smtp.gmail.com', 587)

                s.starttls()

                s.login("info.acdtest@gmail.com", "Dob11011993")

                message = "Accident Detected"

                s.sendmail("keralamanirajendran17@gmail.com", "dummyidnisha0@gmail.com", message)

                s.quit()
                #messagebox.showerror("Accident", "Accident Detected")


            except:
                pass
           # frame = cv2.putText(frame, "28° 35' 31.7040'' N and 77° 2' 45.7836'' E. ; ",
                               # (40, 80), font, fontScale, color, thickness, cv2.LINE_AA, False)
           # frame = cv2.putText(frame, "time:1600 hrs; ", (40, 100),
                               # font, fontScale, color, thickness, cv2.LINE_AA, False)
           # frame = cv2.putText(frame, "camera id:DWARKA_ROAD_22", (40, 120),
                               # font, fontScale, color, thickness, cv2.LINE_AA, False)

        cv2.imshow("Accident detection", frame)

        count += 1

        if cv2.waitKey(33) & 0xff == 27:
            break

    else:
        break

#2 addresss
#testing
#integrate
#