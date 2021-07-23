# {}는 딕셔너리 [] 리스트 
y = {1: 'one', 2: 'two', 3: 'three'}

for i in y.values():
    print(i)


keys = ['a', 'b', 'c', 'd']
print("1차 for >> ")
for value in dict.fromkeys(keys).items():
    print(value, sep='\n\n')

print()

x = {key: value for key, value in dict.fromkeys(keys).items()}
print("key,value 컴프레인션 >> ", x)


j = {'a': 10, "b": 20, 'c': 30, 'd': 40}
# print("iterator 에러")
# for key, value in j.items():
#     if value == 20:
#         del j[key]
#     print(j)


j = {key: value for key, value in j.items() if value != 20}
print("컴프레이션 조건 제거 >> ", j)

testspace_source = {
    "Mercury": {
        "mean_radius": 2440.7,
        "mess": 3.1231*23,
        "orient": 48.234
    },
    "Venus": {
        "mean_radius": 123440.7,
        "mess": 3.23231*23,
        "orient": 54.234
    },
    "Earth": {
        "mean_radius": 123440.7,
        "mess": 3.2331 * 23,
        "orient": 54.24
    },
    "Mars": {
        "mean_radius": 12340.7,
        "mess": 3.21331 * 23,
        "orient": 54.24
    }
}
# 딕셔너리 안에 딕셔너리 호출
print("test 기본값 >> ", testspace_source)
print(testspace_source["Venus"]["mean_radius"])