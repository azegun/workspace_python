def get(key, dataset):
    try:
        print("value 들어가기 전  >> ", key, dataset)
        value = dataset[key]

        print("value 값 입력 후 >> ", value)
    except IndexError:  # 인덱스가 잘못된 예외
        return "인덱스 에러"
    except KeyError:
        return "key 에러"
    else:
        return value


print("인덱싱 에러 확인:  >> ", get(3, (1, 2, 3)), end='\n\n')  # 인덱스가 오버되면 에러
print("key 에러 확인:  >> ", get('age', {'name': '박연오', 'age': 20}))  # 튜플안에 key가 없으면 에러