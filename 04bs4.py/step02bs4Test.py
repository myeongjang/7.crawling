#? bs4 import
from bs4 import BeautifulSoup
#? file : open(), 한글이 내장된 파일
file1 = open('step02bs4Test.html', encoding = "utf-8")
#? html.parser 타입으로 bs4 객체 생성(soup)
soup = BeautifulSoup(file1, "html.parser")

#step01 : css 선택자로 데이터 추출하기
#string
print(soup.select_one("li:nth-of-type(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)
#step02 : find 함수로 추출하기
"""
복잡한 문서에는 중복된 속성들 다수 존재
이 경우 다수의 속성으로 검색해야 할 경우 발생
dict 타입으로 속성들 구성후에 검색해 보기
"""
attDatas = {"data-lo" : "us", "class": "black"}
print(soup.find("li", attDatas).string)

#step03 : find 함수로 연속적으로 추출하기
print(soup.find(id="ve-list").find("li", attDatas).string,'연속사용')