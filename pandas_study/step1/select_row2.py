import pandas as pd

exam_data = {
    '이름': ['서준', '우현', '인아'],
    '수학': [90, 80, 70],
    '영어': [98, 89, 95],
    '음악': [85, 95, 100],
    '체육': [100, 90, 90]
}

df = pd.DataFrame(exam_data)
print('exam_data', df, sep='\n', end='\n\n')

print("# 수학 점수 데이터만 선택. 변수 math1에 저장")
math1 = df['수학']
print('math1', type(math1), math1, sep='\n', end='\n\n')

print("# 영어 점수 데이터만 선택. 변수 english에 저장")
english = df.영어
print('english', type(english), english, sep='\n', end='\n\n')

print("# 음악, 체육 점수 데이터를 선택. 변수. music_gym에 저장")
music_gym = df[['음악', '체육']]
print('music_gym', type(music_gym), music_gym, sep='\n', end='\n\n')

print("# 수학 점수 데이터만 선택. 변수 math2에 저장")
math2 = df[['수학']]
print('math2', type(math2), math2, sep='\n', end='\n\n')