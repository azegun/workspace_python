import numpy as np

arr = np.random.normal(10, 5, (3, 3))  # 평균이 10, 표준편차가 5
print(arr, end='\n\n')


arr1 = np.random.randint(1, 10, (2, 5))
arr2 = np.random.randint(10, 20, (2, 5))
print(arr1, end='\n\n')
print(arr2, end='\n\n')
print("====================")
print(arr1 + arr2)
divided = (arr1 + arr2) / 2
print("============나누기===========")
divided = np.array(divided, dtype=np.int32)  #  int값으로 변경
print(divided, type(divided[0, 0]), end='\n\n\n')

date = np.array('2021-07-26')
print(date)     
date = np.array(date, dtype=np.datetime64)   # datetime64로 변경
print(date.dtype, date + 10)   # 타입 변경시 연산 가능
date2 = np.array('2022-07-25', dtype=np.datetime64)
print(date2-date)  # 타입 맞추면 브로드캐스팅 가능
