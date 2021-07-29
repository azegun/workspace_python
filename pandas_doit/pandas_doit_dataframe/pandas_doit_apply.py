import pandas as pd
import seaborn as sns
import numpy as np


def my_sq(x):
    return x ** 2


def my_exp(x, n):
    return x ** n


def avg_3(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z)/3


df = pd.DataFrame({'a': [10, 20, 30],
                   'b': [20, 30, 40]})
# print(df, end='\n\n')
#
#
# result = df['a'].apply(my_sq)
# print(result, end='\n\n')
#
# result1 = df['b'].apply(my_sq)
# print(result1, end='\n\n')
#
# result2 = df['b'].apply(my_exp, n=3)
# print(result2, end='\n\n')
#
# average = df.apply(avg_3)
# print(average, end='\n\n')

titanic = sns.load_dataset('titanic')


def count_missing(vec):
    # vec = titanic
    null_vec = pd.isnull(vec)
    # null의 개수 count
    null_count = np.sum(null_vec)
    return null_count


# 누락값들의 비율울 확인하는 method
def prop_missing(vec):
    # 컬럼마다 null 개수를 출력
    num = count_missing(vec)
    # 컬럼 전체의 사이즈
    dem = vec.size
    return(num / dem) * 100


# 누락값이 아닌 데이터값을 출력
def prop_complete(vec):
    return 1 - prop_missing(vec)


# print(titanic)
cmis_col = titanic.apply(count_missing)
print("cmis_col >>", cmis_col, end='\n\n')

cmis_prop = titanic.apply(prop_missing)
print("cmis_prop >>", cmis_prop, end='\n\n')

complete_prop = titanic.apply(prop_complete)
print("complete_prop >>", complete_prop, end='\n\n')

# axis =1는 열
titanic['num_missing'] = titanic.apply(count_missing, axis=1)
print(titanic, end='\n\n')

# missing이 1이상, 행열 전체를 출력
print(titanic.loc[titanic['num_missing'] > 1, :].sample(10))

