from selenium import webdriver
import time

#step01 : 네이버 사이트 실행하기
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("http://127.0.0.1:5500/5.selenium/step03myHtml.html")

tag = driver.find_element_by_id("btn")
tag.click() # onclick 속성으로 구현된 tag 클릭 기능

time.sleep(3)
driver.close()