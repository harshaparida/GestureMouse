import numpy as np
import cv2
import HandTrackingModule as htm
import time
import pyautogui


wCam, hCam = 640, 480
frameR = 100

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.HandDetector(maxHands=1)
wScr, hScr = pyautogui.size()
print(wScr, hScr)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if len(lmList)!= 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]
        print(x1, y1, x2, y2)

        fingers = detector.fingersUp()
        #print(fingers)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam-frameR),
                          (255,0,255), 2)
        if fingers[1] == 1 and fingers[2] == 0:
            
            x3 = np.interp(x1, (0,wCam), (0,wScr))
            y3 = np.interp(y1, (0,hCam), (0,hScr))
            pyautogui.moveTo(wScr - x3, y3)
            cv2.circle(img, (x1, y1), 15,(255,0,255), cv2.FILLED)
        

    # frame rate
    cTime = time.time();
    fps = 1/(cTime-pTime);
    pTime = cTime;
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255,0,0), 3)



    cv2.imshow("Image", img)
    cv2.waitKey(1)
    







