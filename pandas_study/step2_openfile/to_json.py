import pandas as pd


#판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {
    'name': ['Jerry', 'Riah', 'Paul'],
    'algol': ["A", "A+", "B"],
    'basic': ["C", "B", "B+"],
    'c++': ["B+", "C", "C+"]
}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)  # name 열을 인덱스로 저장
print(df)

print("# to_csv() 메소드를 사용하여 CSV파일로 보내기. 파일명은 df_sample.csv로 지정")
df.to_json("./df_sample.json")