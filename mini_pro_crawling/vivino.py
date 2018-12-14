#vivino 
import time #딜레이를 하기 위한 time import
import re #정규식을 이용하여 url 주소 중 일부분만 추출하기 위한 용도
from bs4 import BeautifulSoup # 크롤링 할떄 쓰이는 유용한 라이브러리
from selenium import webdriver # web을 작동 시키기 위한 라이브러리
from selenium.webdriver.common.by import By 
from pymongo import MongoClient # mongodb라는 nosql데이터 베이스

from selenium.webdriver.support.ui import WebDriverWait

def main():
    
    search()
    wine_crawler()



def search():
    driver.get(main_url)
    driver.implicitly_wait(10)
    time.sleep(3)
    try:
        elem = driver.find_element_by_class_name("searchBar__searchInput--2aCeZ")
        elem.clear()
        elem.send_keys(keyword)
        elem.submit() 
        
       
    except AttributeError:
        print("잘못된 검색어를 입력하셨습니다.")
    
    

def wine_crawler():    
    
    try:
        maxlen = int(input("어디 페이지 까지 검색하실 건가요?"))
        count = 0
        for i in range(1,maxlen+1):
            soup = BeautifulSoup(driver.page_source, "lxml" )
            driver.implicitly_wait(3)
            wine_items = soup.select(".default-wine-card")
            for wine in wine_items:
                img_ex = wine.find("figure")['style']
                img = re.findall("[/][/].+g",img_ex)
                url = wine.find('a')['href']
                title = wine.select(".link-color-alt-grey > .bold")[0].text.replace("\n","")
                region = wine.select(".link-color-alt-grey")[1].text
                country = wine.select(".link-color-alt-grey")[2].text
                rating = wine.select(".text-inline-block")[0].text.strip().replace(" ","")
                price = wine.select(".wine-price-value")[0].text.replace("—","0")
                url = main_url+url
                wineInfo = {
                    'ImageURL' : "https:"+img[0],
                    'URL' : url,
                    'Name' : title,
                    'Origin' : country,
                    'Rate' : rating,
                    'Price' : price 
                }
                
                collection.insert_one(wineInfo)
                count += 1
                print(str(count)+"번째")
                print("와인 이미지 : https:"+img[0])
                print("링크 주소 : ", url)
                print("와인이름 :",title)
                print("원산지 :",region)
                print("국가 : ",country)
                print("평균 점수 : ",rating)
                print("평균 가격 :",price)
                print("***************************")

                driver.implicitly_wait(3)
            driver.find_element_by_xpath('//*[@id="next"]').click()
            
                
    except Exception:
       print("이 과정을 실행 할 수 없습니다.....")
    finally:
        time.sleep(3)
        driver.close()   
            
if __name__ == "__main__":
    main_url = "https://www.vivino.com/" # 메인 url 주소
    keyword = input("무엇을 검색 하시겠습니까?") #홈페이지 내 검색할 키워드 입력

    driver = webdriver.Chrome("C:/driver/chromedriver.exe") #크롬으로 진행
    driver.get(main_url) # 실행

    client = MongoClient('localhost', 27017) #mongo 연결
    db = client.project #데이터 베이스 만들기
    collection = db.crawling # table(collection) 만들기
    
    main()
    



                 e