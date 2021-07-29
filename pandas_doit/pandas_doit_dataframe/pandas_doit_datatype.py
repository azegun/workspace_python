import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')
# type category str에 비해 용량이 적음.
# categoty는 object로 바꿔줘야함.
# print(tips['sex'].memory_usage())

# tips['sex'] = tips['sex'].astype(object)
# print(tips['sex'].memory_usage())
# print(tips.dtypes)

print(tips)
print(tips.loc[[1, 2], 'total_bill'])

# 문자 가 일부만 들어가도 컬럼이 object로 변경
tips.loc[[1, 2], 'total_bill'] = '오입력'
print(tips.dtypes)
tips['total_bill'] = tips['total_bill'].astype(float)
# print(tips['total_bill'].astype(float))
print(pd.to_numeric(tips['total_bill'], errors='ignore'))
print(tips.dtypes)
# print(tips['total_bill'])
