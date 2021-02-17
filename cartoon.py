import cv2
import sys

from filtering import filter
from color_reduction import cube_reduction
from increase_trickness import trickness
from saturation import saturation


def pipeline(frame):
    filtered = filter(frame)
    trick = trickness(filtered)
    reduced = cube_reduction(filtered)
    satur = saturation(reduced) 
    #cv2.imwrite('t.png', trick)
    #exit(0)
    return filtered


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
    out = cv2.VideoWriter('output/output.mp4', fourcc, fps, size)

    while True:
        ret, frame = cap.read()
        
        if frame is None:
            break

        processed = pipeline(frame)
        out.write(processed)

    cap.release()
    out.release()


__init__(sys.argv[1])
