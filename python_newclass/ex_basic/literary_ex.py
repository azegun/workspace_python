# 문자열 인덱싱
letters = 'python'
print("문자 인덱싱 뽑기 >>", letters[0], letters[2], end='\n\n')

string = "홀짝홀짝홀짝"
print("홀홀홀만 뽑기 >> ", string[::2])
print("거꾸로 >> ", string[::-1], end='\n\n')

# 문자열 리플레이스(치환)
phone_number = "010-1111-2222"

phone_number1 = phone_number.replace("-", " ")
print("문자열 치환>> ", phone_number1)

phone_number2 = phone_number.replace("-", "")
print("문자열 치환2 >>", phone_number2)

string = 'abcdfe2a354a32a'
print("문자열 치환3 >> ", string.replace('a', 'A'))

string = 'abcdfe2a354bba32a'
print("문자열 치환4 >> ", string.replace('b', 'B'), end='\n\n')

# 스플릿으로 나누기
url = "http://sharebook.kr"
print("스플릿으로 나누기 >> ", url.split('.')[-1], end='\n\n')  # ['http://sharebook', 'kr']

# 문자열 곱하기
print("-" * 80)

t1 = 'java'
t2 = "python"
print((t2 + ' ' + t1 + ' ') * 3, end='\n\n')

name1 = "김민수"
name2 = "이철희"
age1 = 10
age2 = 20
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
print("포맷>>>>>>>>>> ")
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
print("f-string")
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}",end='\n\n')

# 제거하고 -> 타입변경
qty = "5,969,782,550"
removecomma = qty.replace(",", "")
print("콤마 제거 >>", removecomma, type(removecomma))
convert = int(removecomma)
print("정수 변경 >>", convert, type(convert), end='\n\n')

# 슬라이싱
qt = "2020/03(E) (IFRS연결)"
print("qt슬라이싱 >> ", qt[:7], end='\n\n')

# strip --> trim
data = "   삼성전자    "
print("data >> ", data, "change >> ", data.strip(), end='\n\n')

# 소문자, 대문자 변경
ticker = "btc_krw"
print("대문자 >>", ticker.upper(), "소문자 >> ", ticker.lower())
print("capitailize()는 맨앞자리를 대문자 >> ", ticker.capitalize(), end='\n\n')

# 스트링 내용 부분으로 확인
file_name = "보고서.xlsx"
print("endswith>> ", file_name.endswith("xlsx"))  # True

file_name = "2020_보고서.xlsx"
print("startswith  >> ", file_name.startswith("2020"), end='\n\n')

# split 분리 시키면 리스트로 받음
a = "hello world"
print("split-----------")
print("공백 분리 >> ", a.split())
print("_ 분리 >> ", ticker.split("_"))

date = "2020-05-01"
print("- date 분리 >> ", date.split("-"))
print("-----------------", end='\n\n')

data = "039490     "
print("rstrip >> ", data)