import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../pandas_doit_basic/data/scientists.csv')
print(df, end='\n\n')

age = df['Age']
born = df['Born']
print("==============평균===========")
print(age.mean(), end='\n\n')

result = age > age.mean()

print(df[result], end='\n\n')

print(age + age, end='\n\n')
print()



