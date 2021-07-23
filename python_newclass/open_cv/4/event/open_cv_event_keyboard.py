import numpy as np
import cv2

# switch case문을 사전(dic)으로 구성
switch_case = {
    ord('a'): "a키 입력",       # ord()함수 : 문자 -> 아스키코드 변환
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",   # 0ㅌ42(16진수) -> 10진수 변환
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image = np.ones((200, 300), np.float) # 원소값 1인 행렬 생성
cv2.namedWindow("Keyboard Event")
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)        # 100ms동안 키 이벤트 대기
    if key == 27: break             # esc키 누르면 종료

    try:
        print("key >> ", key)
        result = switch_case[key]
        print("result >> ", result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()