# person_data = ['홍길동', 15, '서울시']
# 매개변수로 넣어서 for로 돌리는게 수월함
# def personal_info(*args):               # *args = *person_data
#     for arg in args:
#         print(arg)

# 기본 가변인수
# def personal_info(name, age, address):
# print('이름: ', name)
# print('나이: ', age)
# print('주소: ', address)

# personal_info(*person_data)


# 매개변수 설정은 기본값, 만약 밑에서 다시 설정하면 그 값을 받음





# personal_info('강감찬', 14, address='대전')

# 리스트는 * 1개, 딕셔너리는  ** 2개
person_data = ['을지야', 25, '대구시']
person_data_dict = {'name': '홍길동', 'address': '서울시', 'age': 15}

def personal_info(name, age, address):
    print(name)
    print(age)
    print(address)


personal_info(*person_data)
print()
personal_info(**person_data_dict)