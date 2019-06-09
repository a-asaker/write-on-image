#!/usr/bin/env python3
import cv2
import numpy as np
import sys

font = cv2.FONT_HERSHEY_COMPLEX
# mouse callback function
def write(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        i = 0
        cap=0
        k=""
        while True:
            k = cv2.waitKey(0)
            if k == 27:
                break
            elif k in [225,226]:
                k = cv2.waitKey(0)-32
            elif k is 229:
                cap = not cap
                k = 0
            elif k is 13:
                y+=68
                i = 0
                k = 0
            elif k is 8:
                cv2.rectangle(img, (x+i-42,y-48),(x+i+20,y+20), (0,0,0), -1, cv2.LINE_AA)
                k=0
                i-=80
            if cap :
                k = k-32
            try:
                cv2.putText(img, chr(k) , (x+i,y), font,2, (0,0,255), 10, cv2.LINE_AA)
                cv2.putText(img, chr(k) , (x+i,y), font,2, (255,0,0), 5, cv2.LINE_AA)
                i+=40
            except:
                i+=40
            cv2.imshow('image',img)

if len(sys.argv)==2:
	img = cv2.imread(sys.argv[1])
else:
	img = np.zeros((960,1100,3), np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',write)
while True:
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k == 27:
        break
    elif k in [115,83]:
        cv2.imwrite('img.png',img)
cv2.destroyAllWindows()
