import cv2
import numpy as np


def saturation(frame):
    imghsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv2.split(imghsv)
    s = s * 1.5
    s = np.clip(s, 0, 255)
    imghsv = cv2.merge([h,s,v])
    imgbgr = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

    return imgbgr
