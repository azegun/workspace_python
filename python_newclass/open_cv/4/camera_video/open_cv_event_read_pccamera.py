from cv2 import *


def put_string(frame, text, pt, value, color=(120, 200, 90)):             # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    print("pt[0]. pt[1]", pt[0], pt[0])
    font = FONT_HERSHEY_SIMPLEX
    putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기


capture = VideoCapture(0)  # 1. 0번 카메라 연결
if capture.isOpened() == False:   # 카메라 연결 예외 처리
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(CAP_PROP_BRIGHTNESS))
while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if waitKey(30) >= 0: break   # 종료 조건 - 스페이스바키

    exposure = capture.get(CAP_PROP_EXPOSURE)
    put_string(frame, "EXPOS: ", (10, 40), exposure)
    title = "View Frame from Camera"
    imshow(title, frame)  # 윈도우에 영상 띄우기

capture.release()