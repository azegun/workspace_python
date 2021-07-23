import tkinter
import cv2
import time

import PIL.Image, PIL.ImageTk
from MyVideoCapture import *


class tkCamera(tkinter.Frame):
    def __init__(self, window, text="", video_source=0, width=None, height=None, repeat=0):

        super().__init__(window)

        self.window = window

        self.repeat = repeat
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source, width, height)

        self.label = tkinter.Label(self, text=text)
        self.label.pack()

        self.canvas = tkinter.Canvas(self, width=self.vid.width *2, height=self.vid.height)
        self.canvas.pack()

        self.btn_start = tkinter.Button(self, text="Start", command=self.start)
        self.btn_start.pack(anchor="center", side="left")

        self.btn_stop = tkinter.Button(self, text="Stop", command=self.stop)
        self.btn_stop.pack(anchor="center", side="left")

        self.btn_snapshot = tkinter.Button(self, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(anchor="center", side="left")
        
        # 호출된 후  fps를 이용하여 자동 지연시킴
        self.delay = int(1000/self.vid.fps)

        print("[tkCamera] source : ", self.video_source)
        print("[tkCamera] fps : ", self.vid.fps, "delay: ", self.delay)

        self.image = None

        self.running = True
        self.update_frame()

    def start(self):
        if not self.running:
            self.running = True
            self.update_frame()

    def stop(self):
        if self.running:
            self.running = False

    def snapshot(self):
        if self.image:
            self.image.save(time.strftime("frame-%d-%m-%Y-%H-%M-%S.jpg"))
        # ret, frame = self.vid.get_frame()
        #
        # if ret:
        #     cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update_frame(self):
        ret, frame = self.vid.get_frame()
        # 엣지 검출
        # if self.repeat == 1:
        #     rep_image = cv2.repeat(frame, 1, 2)
        #     rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)
        #     rep_edge = cv2.GaussianBlur(frame, (5, 5), 0)
        #     rep_edge = cv2.Canny(frame, 50, 100, 5)
        #     h, w = frame.shape[:2]
        #     cv2.rectangle(frame, (0, 0, w, h), 255, -1)
        #     color_edge = cv2.bitwise_and(frame, frame, mask=rep_edge)

        if ret:
            self.image = PIL.Image.fromarray(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        if self.running:
            self.window.after(self.delay, self.update_frame)

