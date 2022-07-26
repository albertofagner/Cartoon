import cv2
import numpy as np


def trickness(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sobelx = np.uint8(np.absolute(sobelx))
    sobely = np.uint8(np.absolute(sobely))

    sobelxy = sobelx + sobely

    _, thresh = cv2.threshold(sobelxy, 70, 255, cv2.THRESH_BINARY)

    return thresh
