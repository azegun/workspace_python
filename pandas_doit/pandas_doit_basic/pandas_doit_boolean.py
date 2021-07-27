import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../pandas_doit_basic/data/scientists.csv')
print(df, end='\n\n')

age = df['Age']
print("==============평균===========")
print(age.mean(), end='\n\n')

result = age > age.mean()

print(df[result])