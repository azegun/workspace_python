import json
import pickle

# Json으로 파일 받기

customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
# 바이너리 쓰고, 읽기 @pickle - 바이너리
with open("../data.pkl", "wb") as file:
    pickle.dump(customer, file)  # 인코더


with open("../data.pkl", "rb") as file:
    dictionary = pickle.load(file)   # 디코더

print(dictionary)


a_file = open("../data.pkl", "wb")
pickle.dump(customer, a_file)  # 인코더
a_file.close()


# JSON 인코딩
jsonString = json.dumps(customer)

file = open("../../test2.txt", "w")
# 인용코드 상관없이 작성할떄는 앞뒤 끝에 ''' '''
file.write(jsonString)
file.close()

# 읽어오기
file = open("../../test2.txt", "r")
s = file.read()
print(s)
file.close()

# with open!!
with open("../../test2.txt", "r") as file:
    s = file.read()
    print(s)

# 반복문
with open("../../test2.txt", "w") as file:
    for i in range(3):
        file.write('hello, world! {0}\n'.format(i))


# 리스트 안에 있는 문자열 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open("../../test2.txt", "w") as file:
    file.writelines(lines)


with open("../../test2.txt", "r") as file:
    lines = file.readlines()
    print(lines)


# 파일 내용 한 줄씩 읽기
with open("../../test2.txt", "r") as file:
    line = None
    while line != '':
        line = file.readline()
        # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
        print(line.strip('\n'))

# 미완성
lines1 = [['10', '20', '30'], ['50', '60', '70']]

# with open("hello.txt", "w") as file:
#     for lines1 in file:
#         read = file.writelines(lines1)
#     # for lines1 in file:


# print("읽기")
#
# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line.strip('\n'))

name = "james"
age = 17
address = "서울시 서초구 반포동"
scores = {"korean": 90, "english": 95, "mathematics": 85, "science": 82}

with open("../james.p", "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


with open("../james.p", "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores, type(scores))

for key in dict.fromkeys(scores).keys():
    print(key)





