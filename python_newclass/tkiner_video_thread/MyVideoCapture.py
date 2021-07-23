import cv2
import numpy as np


class MyVideoCapture:
    def __init__(self, video_source=0, width=None, height=None):

        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = width
        self.height = height

        # Get video source width and height
        if not self.width:
            self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))  # convert float to int
        if not self.height:
            self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))  # convert float to int

        self.ret = False
        self.frame = None

    def process(self):
        ret = False
        frame = None

        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.Laplacian(frame, cv2.CV_16S, 1)
        self.ret = ret
        self.frame = frame

    def get_frame(self):
        self.process()  # later run in thread
        return self.ret, self.frame

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()