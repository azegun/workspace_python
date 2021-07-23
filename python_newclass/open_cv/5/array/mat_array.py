import cv2

image = cv2.imread(
    "images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리

x_axis = cv2.flip(image, 0)                 # x축 기준 상하 뒤집기
y_axis = cv2.flip(image, 1)                 # y축 기준 좌우 뒤집기
xy_axis = cv2.flip(image, -1)               # x축 y축 둘다 뒤집기
rep_image = cv2.repeat(image, 1, 2)       # 반복 복사
trans_image = cv2.transpose(image)          # 행렬 전치

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']  # 리스트 안에 타이틀 별로 입력
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)
# a = eval('image')
# exex(a = 'image')