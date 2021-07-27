import pandas as pd

df = pd.read_csv('../pandas_doit_basic/data/scientists.csv')
print(df, end='\n\n')

df_name = df['Name']
df_born = df['Born']
df_born.to_pickle('../pandas_doit_basic/save/born.pickle')
df_name.to_pickle('../pandas_doit_basic/save/name.pickle')

df_read = pd.read_pickle('../pandas_doit_basic/save/name.pickle')
print("=========pickle========")
print(df_read, end='\n\n')
print(df_born, end='\n\n')

df.to_csv('../pandas_doit_basic/save/1.csv')
read_df = pd.read_csv('../pandas_doit_basic/save/1.csv')
print(read_df, end='\n\n')

df_job = df[['Name', 'Occupation']]
df_job.to_csv('../pandas_doit_basic/save/job.csv')
print()

read_job = pd.read_csv('../pandas_doit_basic/save/job.csv')
print(read_job)


# 엑셀 저장/ 읽기 할떄 필요한 라이브러리
# pip install xlwt  xls  2007 이전 필요 라이브러리
# pip install openpyxl  xlsx  2007 이후 필요 라이브러리
# pip install xlrd 읽기

df.to_excel('../pandas_doit_basic/save/test_excel.xls')
df.to_excel('../pandas_doit_basic/save/test_excel.xlsx')

read_excel1 = pd.read_excel('../pandas_doit_basic/save/test_excel.xlsx')
read_excel = pd.read_excel('../pandas_doit_basic/save/test_excel.xls')
print("엑설 리드1 > > > ", read_excel1)
print("액셀 리드2 > > >", read_excel)