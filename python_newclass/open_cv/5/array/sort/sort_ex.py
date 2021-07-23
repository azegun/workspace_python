import numpy as np, cv2

m = np.random.randint(0, 100, 15).reshape(3, 5) # 임의 난수 생성

m_sort1 = cv2.sortIdx(m, cv2.SORT_EVERY_ROW)       # 행단위 오름차순
m_sort2 = cv2.sortIdx(m, cv2.SORT_EVERY_COLUMN)  # 열단위(세로) 오름차순
m_sort3 = np.argsort(m, axis=0)                 # 행단위(가로) 내림차순
m_sort4 = np.sort(m, axis=0)                         # 세로축 정렬
m_sort5 = np.sort(m, axis=0)                         # 가로축 정렬
m_sort6 = np.sort(m, axis=1)[:, ::-1]         # 가로축 내림차순 정렬

titles = ['m', 'm_sort1', 'm_sort2', 'm_sort3', 'm_sort4', 'm_sort5', 'm_sort6']
for title in titles:
    print("[%s] = \n%s\n" %(title, eval(title)))

