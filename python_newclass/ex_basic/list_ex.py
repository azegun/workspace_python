# 리스트 선언
from numpy import interp

movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print("list 선언 >> ", movie_rank)

# 리스트 추가
movie_rank.append("베트맨")
print("append>> ", movie_rank)

# 중간에 추가
movie_rank.insert(1, '슈퍼맨')
print("insert 리스트 중간에 >> ", movie_rank)

# 삭제
movie_rank.pop(3)
print("삭제 pop >> ", movie_rank, end="\n\n")

# 두개 리스트를 합친다
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print("리스트 합치기 >> ", langs, end="\n\n")

# 최댓값, 최솟값, 합계, 평균
nums = [1, 2, 3, 4, 5, 6, 7]

print("max >> ", max(nums), " min >> ", min(nums))
print("sum() >> ", sum(nums))
average = sum(nums) / len(nums)
print("avg() >> ", average, end="\n\n")

# 리스트 길이구하기, 사이즈랑 동일
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print("len() >> ", len(cook), end="\n\n")

# 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print("1번 인덱스부터 출력 >> ", price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("홀수만 출력 >> ", nums[::2])
print("짝수만 출력 >> ", nums[1::2])
print("거꾸로 출력 >> ", nums[::-1], end="\n\n")

# 리스트 선택자
interest = ['삼성전자', 'LG전자', 'Naver']
interest.pop(1)
print("삭제하고 >> ", interest)
print("선택자 >> ", interest[0], interest[1], end="\n\n")

# join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("조인 메서드1>> ", " ".join(interest))
print("조인 메서드2>> ", "/".join(interest))
print("조인 메서드3")
print("\n".join(interest), end="\n\n")

# 문자열 split
string = "삼성전자/LG전자/Naver"
print("문자열 split >> ", string.split("/"), end="\n\n")

# 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print("정렬 sort >> ", data )

