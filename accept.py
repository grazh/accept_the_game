import pyautogui as pp
import cv2

img = cv2.imread('scott.jpeg', -1)
cv2.imshow('Waiting fot game...', img)

while 1:
    pp.moveTo(960, 540)
    pp.click()
    k = cv2.waitKey(10000) & 0xFF
    if (k != 255):
        break
cv2.destroyAllWindows()