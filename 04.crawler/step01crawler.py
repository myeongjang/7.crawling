# 새로나온 책 화면에서 각 서적별 링크 url값 스크래핑
# 퍼머링크 출력하기

import requests
import lxml.html
import time
response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
#print(response) #<Response [200]>
root = lxml.html.fromstring(response.content)
#html도 tree 구조 즉 족보 형태(조상, 부모, 자식 관계를 표현)
#최상위 root html tag
# tag 용어는 element라고도 함
#html tag 최상위ㅣ tag, 자식 자손 
#print(root)
#크롤링한 모든 데이터
#print(response.content)

#모든 url을 절대 경로의 url로 반환
root.make_links_absolute(response.url)
tic = time.time()
for a in root.cssselect('.view_box .book_tit a'):
    url  = a.get('href')
    print(url)
print((time.time() - tic) *10000)