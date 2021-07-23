import requests
from bs4 import BeautifulSoup

# 웹 페이지를 가져온 뒤 BeatifulSoup 객체로 만듦
response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp') # 홈페이지를 가져옴
soup = BeautifulSoup(response.content, 'html.parser')  # html을 파싱

table = soup.find('table', {'class': 'table_develop3'})

data = []                               # 데이터를 저장할 리스트
for tr in table.find_all('tr'):         # 모든 <tr> 태그르 찾아서 반복
    tds = list(tr.find_all('td'))       # 모든 <td> 태그를 찾아서 리스트 만듦
    for td in tds:
        # print("td>> ", td)
        # print("tds>>", tds)
        if td.find('a'):
            point = td.find('a').text   # <a> 태그 확인 지점을 찾기
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])  # 리스트에 모든 출력 데이터 입력.

print(data[19]) # 대구지역

with open('../weather.csv', 'w') as file:
    file.write('[point]  [temperature]    [humidity]\n')
    for i in data:
        file.write('{0},         {1},            {2}\n'.format(i[0], i[1], i[2]))
