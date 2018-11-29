#BeautifulSoup import
from bs4 import BeautifulSoup

#html 문서의 tree 구조 이해하기 + BeautifulSoup 활용하기
html='''
<html>
    <body>
        <h1>스크래핑이란?</h1>
        <p id="one">웹페이지1</p>
        <p id="two">웹페이지2</p>
        <span>
            <p>웹페이지3</p>
        </span>
    </body>
</html>
'''
#크롤링한 데이터와 사용할 parser로 객체 생성
soup = BeautifulSoup(html,"html.parser")
#print(soup.html)
print("---------------step04 : 미션--------------")
#select* 관련 함수 중에 list 반환이 아닌 단수 형태의 요소를 반환하는 함수
#<p id="two">웹페이지 2</p> 검색 및 text값 출력 
text = soup.select_one("#two").string
print(text)
print("----------step03 : a 앵커 [하이퍼링크, 링크] tag의 href 속성값 및 text")
#find_all() : 모든 a tag를 리스트에 저장해서 반환
links = soup.find_all("a")
#print(links)
for a in  links:
    href = a.attr['href']
    text = a.string
    #print("*** ", href, "---", text)



print("-----------step02 : find() 함수 -----------------")
#print(soup.find(id="one"))
#print(soup.find(id="one").string)
#print(soup.select(".redColor"))
#웹페이지3
'''
select() : css selector 사용 가능한 API
         : 반환타일 list
         : ㅅ용
'''

print("-----------step01-----------------")
#print(soup.html.h1)
#print("==============")
#print(type(soup.html.p))
##print('-', soup.html.p.next_sibling.next_sibling, '-')
print("==============")

#print(soup.html.span.p.string)#웹페이지3
#print(soup.html.span.p.get_text())#웹페이지3


