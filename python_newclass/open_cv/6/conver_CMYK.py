import numpy as np, cv2

BGR_img = cv2.imread("images/color_model.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
CMY_img = white - BGR_img
print("CMY_img >> ", CMY_img)
CMY = cv2.split(CMY_img)            # 채널 분리
print("CMY >>", CMY)

black = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))        # 원소 간의 최솟값 저장
Yellow, Margenta, Cyan = CMY - black                    # 3개 행렬 최소값 치분

titles = ['black', 'Yellow', 'Margenta', 'Cyan']
[cv2.imshow(t, eval(t)) for t in titles]
# for t in titles:
#     cv2.imshow(t, eval(t))
# print("t>> ", t)


cv2.waitKey(0)