import matplotlib.pyplot as plt
import numpy as np

# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)
print(t)
# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 지점마다 포커싱포인트
# plt.xlabel('X-Label')      # 부가 설명
# plt.ylabel('Y-Label')
# plt.axis([0, 5, 0, 20])
plt.show()