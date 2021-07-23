# 별 표현식
a, b, *c = (0, 1, 2, 3, 4, 5)
print("별 표현식1 * >> ", a, b, c) #  a = 0, b = 1, c= [2, 3, 4, 5]

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]
*a, _, _ = scores
print("별 표현식2 * >> ", a)

a, b, *valid_score = scores
print("별 표현식3 * >>", valid_score)

a, *valid_score, b = scores
print("별 표현식4 * >>", valid_score, end='\n\n')

# 딕셔너리
temp = {}
print("dictionary empty >> ",  temp, type(temp), end='\n\n')

ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print("ice dic{} >> ", ice)

ice['죠스바'] = 1200
ice['월드콘'] = 1500
print("ice dic() 추가 >> ", ice, end='\n\n')

print("딕셔너리 출력 >> ", "메로나 가격: ", ice['메로나'])

# 딕셔너리는 덮어 씌우면 수정
ice['메로나'] = 1300
print("딕셔너리 수정 >> ", ice)

del ice['메로나']
print("딕셔너리 삭제 >> ", ice, end='\n\n')

# 딕셔너리 key값으로 list 받기
ice_stock = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print("{}key값으로 리스트 출력 >> ", ice_stock)

print("딕셔너리안에 리스트 인덱스로 출력 1 >> ", ice_stock['메로나'][0], '원')
print("딕셔너리안에 리스트 인덱스로 출력 2 >> ", ice_stock['메로나'][1], '개', end='\n\n')
ice_stock['월드콘'] = [500, 7]
print("딕셔너리안에 리스트 추가 >> ", ice_stock, end='\n\n')

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print("keys값들 모두 출력 >> ",  list(icecream.keys()))
print("values값들 모두 출력 >> ",  list(icecream.values()))
print("values값을 더한값 출력 >> ",  sum(list(icecream.values())), end='\n\n')

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수': 2700, '아맛나': 1000}

icecream.update(new_product)
print("딕셔너리 추가 업데이트 >> ", icecream, end='\n\n')

# 튜플 두개를 딕셔너리로 변환
# dict(zip)이 key, value로 딕셔너리 만들어줌
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print("튜플 여러개를 딕셔너리로 변환 >> ", result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print("리스트 여러개를 딕셔너리로 변환 >>", close_table)