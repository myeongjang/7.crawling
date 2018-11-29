from selenium import webdriver
import time

#step01 : 네이버 사이트 실행하기
driver = webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("https://www.naver.com/")
tag = driver.find_element_by_name("query")
tag.clear() # 혹시 내용이 있으면 삭제
tag.send_keys("빅데이터") # 입력
tag.submit()

time.sleep(30)
driver.close()
 
#pip install selenium==3.0

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# def Get_mok():
#     data = []
#     s1 = driver.page_source
#     s2 = BeautifulSoup(s1, "html.parser")
#     s3 = s2.find("div", id = "tabs_3")
#     s3 = s3.text
#     print(s3)
#     driver.back()


def runDriver(url):
    global driver
    driver = webdriver.Chrome(r"C:\0.ITStudy\driver\chromedriver.exe")
    driver.get(url)

def naverConan(question):
    conan = driver.find_element_by_xpath("//*[@id=\"query\"]")
    conan.send_keys("\b"*50)
    conan.send_keys(question)
    driver.find_element_by_xpath("//*[@id=\"search_btn\"]").click()

if __name__ == "__main___":
runDriver("https://www.naver.com/")
