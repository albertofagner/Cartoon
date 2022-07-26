import cv2
import sys
import numpy as np
import os

from filtering import filter
from color_reduction import cube_reduction
from increase_trickness import trickness
from saturation import saturation


def pipeline(frame):
    filtered = filter(frame)
    trick = trickness(filtered)
    reduced = cube_reduction(filtered)
    satur = saturation(reduced)

    result = np.copy(satur)
    result[np.where(trick==255)] = [0,0,0]

    return result


def __init__(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ERROR: Video not Found")
        exit(0)
    
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    if not os.path.exists('output'):
        os.makedirs('output')
    out = cv2.VideoWriter('output/output.mp4', fourcc, fps, size)

    while True:
        _, frame = cap.read()
        
        if frame is None:
            break

        processed = pipeline(frame)
        out.write(processed)

    cap.release()
    out.release()


__init__(sys.argv[1])
