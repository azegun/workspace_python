import re

# 문자로 매칭 확인
print(re.match("Hello", "Hello, world!"))
print(re.search("^Hello", "Hello, world"))  # ^ 맨앞에 문장 비교
print(re.search("world!$", "Hello, world!"))  # $ 맨뒤에 문장 비교
print(re.match("hello|world", "hello"), end='\n\n')  # | or 문장

print(re.match('[0-9]*', '1234'))   # * : 0개 이상의 패턴
print(re.match('[0-9]+', '1234'))   # + : 1개 이상의 패턴
print(re.match('[0-9]+', 'abcd'), end='\n\n')

print(re.match('a*b', 'b'))  # b에는 a가 0개 이상 패턴
print(re.match('a+b', 'b'))  # a가 1 개이상 있어야함
print(re.match('a*b', 'aab'))
print(re.match('a+b', 'aab'), end='\n\n')

print(re.match('abc?d', 'abd'))
print(re.match('ab[0-9]?c', 'ab3c'))  # [0-9] 위치에 숫자가 1개 있으므로 매칭
print(re.match('ab.d', 'abxd'))  # .이 있는 위치에 문자가 1개 있으므로 매칭

print(re.match('h{3}', 'hhhello'))  # h가 몇개인지 확인 후 매칭
print(re.match('(hello){3}', 'hellohellohello'), end='\n\n')

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-0000-0000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '053-660-3143'), end='\n\n')

print(re.match('[a-zA-Z0-9]+', 'Hello1234'))  # a부터 z, A부터 Z, 0부터 9까지


