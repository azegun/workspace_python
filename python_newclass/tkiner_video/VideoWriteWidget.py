import cv2
import time


class VideoWriterWidget(object):
    def __init__(self, video_file_name, src =0):
        self.frame_name = str(src)
        self.video_file = video_file_name
        self.video_file_name = video_file_name + '.avi'
        self.capture = cv2.VideoCapture(src)
        # 프레임 사이즈
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))
        # 코덱
        self.codec = cv2.VideoWriter.fourcc("M", "J", "P", "G")
        self.output_video = cv2.VideoWriter(self.video_file_name,
                                            self.codec, 30, (self.frame_width, self.frame_height))

    def update(self):
        pass

    def show_frame(self):
        pass

    def save_frame(self):
        pass

    def start_recording(self):
        pass


if __name__ == '__main__':
    src1 = 'Your link1'
    video_writer_widget1 = VideoWriterWidget('Camera 1', src1)
    src2 = "Your link2"
    video_writer_widget2 = VideoWriterWidget('Camera 2', src2)
    src3 = 'Your link3'
    video_writer_widget3 = VideoWriterWidget('Camera 3', src3)
