import time
import tkinter
import cv2
import MyVideoCapture as vc
import PIL.Image, PIL.ImageTk  # 이미지 잘라주는 모듈


class App:
    def __init__(self, window, window_title, video_source):
        self.window = window    # Tk()
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = vc.MyVideoCapture(video_source)
        self.canvas = tkinter.Canvas(window,
                                     width=self.vid.width,
                                     height=self.vid.height)
        self.canvas.pack()

        self.btn_snapshot = tkinter.Button(window, text="snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        self.delay = 15
        self.update()
        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",
                        cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)  # 재귀함수


App(tkinter.Tk(), "Tkinter and OpenCV", 0)

