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
print(soup.html)
print("-----------step01-----------------")
print(soup.html.h1)
print("==============")
print(type(soup.html.p))
print('-', soup.html.p.next_sibling.next_sibling, '-')
print("==============")

print(soup.html.span.p.string)#웹페이지3
print(soup.html.span.p.get_text())#웹페이지3

print("-----------step02 : find() 함수 -----------------")
print(soup.find(id="one"))
print(soup.find(id="one").string)
print(soup.select(".redColor"))
