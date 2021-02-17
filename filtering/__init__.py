import cv2


def filter(frame):
    blur = cv2.bilateralFilter(frame, 5, 50, 50)
    return blur
