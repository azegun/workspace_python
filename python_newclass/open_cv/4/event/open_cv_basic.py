import cv2
import numpy as np
import time

image = np.zeros((200, 300), np.uint8)
for i in range(200):
    image.fill(i)   # 0이되면 배경 검정  0~255

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)    # 윈도우 생성 = 크기변경 불가
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)      # 크기 변경 가능

cv2.imshow(title1, image)
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.moveWindow("window title", 750, 280)
# cv2.namedWindow("aaaaaa", cv2.WINDOW_AUTOSIZE)
# cv2.moveWindow("aaaaaa", 800, 300)
