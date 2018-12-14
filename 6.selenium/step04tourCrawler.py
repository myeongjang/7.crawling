#step04tourCrawler.py

'''
학습 방법
1. http://tour.interpark.com/ 사이트에서 '파리' 검색해 보기
2. 소스 실행후 분석하기
3. 정규 표현식을 반영해 보기
   - 팀단위로 하나만이라도 수정후에 제출
    C:\0.ITStudy\99.제출폴더\10.crawling\181203_정규표현식으로변환해보기

'''

# pip install BeautifulSoup4
# pip install selenium
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements

#검색 page가 로딩 되는 시간을 대기하기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 예외 처리를 위한 모듈
from selenium.webdriver.support import expected_conditions as EC

main_url = "http://tour.interpark.com/"
keyword = "파리"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
#time.sleep(3)  # 절대적 : 무조건 정해진 시간(초) 쉬기
driver.implicitly_wait(10) # seconds

# 입력란 찾기 <input id="SearchGNBText" ... >
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword)

# 동작 불가 왜? : 자바스크립트로 구현되어 있기 때문
# elem.submit() 

# 검색 버튼 찾기 <button class="search-btn" ... >
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

'''
1. 검색 후 이동된 화면
2. 검색된 화면 상의 "해외여행" 영역
    - <div class="oTravelBox"></div>
3. div.oTravelBox > ul > li.moreBtnWrap > button
'''
# 검색된 page가 로드되는 시간 대기
# 10 : 초단위
'''
WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를 기다림

By.CLASS_NAME, "oTravelBox"
    - 
    html
        <class_name>
        <.. class="oTravelBox">

'''
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as e:
    print("검색 page 로드시 class 속성이 oTravelBox를 얻으려는 중 예외 발생 : ", e)


# "해외여행 더보기" 버튼 클릭
driver.find_element_by_css_selector("div.oTravelBox > ul > li.moreBtnWrap > button").click()

# 페이지가 다 뜨면 진행 할수 있게 묵시적인 설정
# Selenium에서 브라우저 자체가 웹 요소들을 기다리도록 만들어주는 옵션
# 초단위
driver.implicitly_wait(10) # seconds

# 1~2page의 해외여행 정보 스크래핑
for page in range(1, 2):
    try:
        # 자바스크립트 실행
        driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
        driver.implicitly_wait(5)
        print("{} 페이지로 이동!!!".format(page))

        soup = BeautifulSoup(driver.page_source, "lxml" )

        boxItems = soup.select(".panelZone > .oTravelBox > .boxList > .boxItem")
        
        print(boxItems,"boxItems!!!!!!!!!!!!!!")
        '''
        for boxItem in boxItems:
            img_src = boxItem.find("img")['src']
            link = boxItem.find("a")['onclick']
            proTitle = boxItem.find("img")['alt']
            proComment = boxItem.find("p", {"class":"proSub"}).text
            # select 는 하나라도 리스트로 리턴
            proPrice = boxItem.select(".proPrice")[0].text
            #proPrice = proPrice.replace(" ", "")
            #proPrice = proPrice.replace("\n", "")
            proPrice_pattern = re.compile(r"\s+")
            proPrice = proPrice_pattern.sub("",proPrice)
            tag_period = boxItem.select(".proInfo")[0]
            tag_period.find('span').replace_with('')  # <span> 태그 없애기
            proPeriod = tag_period.text
            proJumsu = boxItem.select(".proInfo")[2].text

            print("썸네일=", img_src)
            print("링크=", link)
            print("상품명=", proTitle)
            print("코멘트=", proComment)
            print("가격=", proPrice)
            print("여행기간=", proPeriod)
            print("평점=", proJumsu)
            print("=" * 100)
    except Exception as e:
       
     print("페이지 파싱 에러", e)
    '''   
    finally:
        time.sleep(3)
        driver.close()
        