import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


test = input('검색할 이름을 입력하세요.')
path = 'C:/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.youtube.com')  # 웹사이트 주소

time.sleep(5)

element = driver.find_element_by_name('search_query')
element.send_keys(test, Keys.ENTER)
# image_link = driver.find_element_by_link_text('이미지')
# image_link.click()
#
# image_tag = driver.find_element_by_class_name('Q4LuWd')
# time.sleep(1)
#
# image_list = []
#
# for i in range(len(image_tag)):
#     image_list.append(image_tag[i].get_attribute('src'))
# print(image_list)
#
# for i, link in enumerate(image_list):
#     urlretrieve(link, './images/{}{}.jpg'.format(test, i+1))

