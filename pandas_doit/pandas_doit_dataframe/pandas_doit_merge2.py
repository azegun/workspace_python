import pandas as pd

df1 = pd.read_csv('../pandas_doit_dataframe/data/survey_person.csv')
df2 = pd.read_csv('../pandas_doit_dataframe/data/survey_site.csv')
df3 = pd.read_csv('../pandas_doit_dataframe/data/survey_visited.csv')
df4 = pd.read_csv('../pandas_doit_dataframe/data/survey_survey.csv')

print(df1, end='\n\n')
print(df2, end='\n\n')
print(df3, end='\n\n')
print(df4, end='\n\n')

# join 같은 merge
merge_df1_df4 = df1.merge(df4, left_on='ident', right_on='person')
print(merge_df1_df4, end='\n\n')

merge_fail = df1.merge(df4, left_on='ident', right_on='quant')
print(merge_fail)

