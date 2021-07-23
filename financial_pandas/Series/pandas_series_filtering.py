from pandas import Series

data = [42500, 42550, 41800, 42550, 42650]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

s = Series(data=data, index=index)
compare = s > 42000
print(s[compare], type(s[compare]), end='\n\n')  # if절 사용하지 않아도 True들 출력


close = [42500, 42550, 41800, 42550, 42650]
open = [42600, 42200, 41850, 42550, 42500]
index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']

open = Series(data=open, index=index)
close = Series(data=close, index=index)

print("종가가 큰 값")
compare = open < close
print(close[compare], end='\n\n')

diff = close - open
print(diff, end='\n\n')
print(diff[compare])

