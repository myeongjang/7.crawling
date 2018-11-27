'''
step04scraper.py
http://www.hanbit.co.kr/store/books/full_book_list.html

1. 파이썬으로 스크래핑 흐름 이해하기
    - 전체도서목록 page -> 각 도서별 링크 정보 스크래핑 해서 -> DB에 데이터 저장하기
    - 실행후 books.db가 존재하는 경로에서 검색
        >sqlite3 books.db
        sqlite>select * from books;
    

2. 스크래핑 해서 저장되는 정보
   리스트의 도서명
   도서명의 하이퍼링크 url 값
  
3. process
    3-1. 웹페이지 추출하기 : fetch()
    3-2. 스크래핑 하기 : scrape()
    3-3. db에 데이터를 저장하기 : save()

4. 구현 함수 상세 내용
    - 각 기능을 함수로 처리 
    4-1. 웹페이지 추출하기 : fetch(url)
        : 매개 변수로 url을 받고 지정한 url의 웹 페이지를 추출

    4-2. 스크래핑 하기 : scrape(html)
        : 매개변수로 html을 받고, 정규 표현식을 사용해 HTML에서 도서 정보 추출

    4-3. 데이터를 저장하기 : save(db_path, data)
        : 매개변수로 저장할 정보를 받고, SQLite 에 저장
'''

import re
import sqlite3
from urllib.request import urlopen
from html import unescape

#로직 - 완성
def main():
    """ 
    fetch(), scrape(), save() 함수를 호출
    """
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')

    books = scrape(html)
    save('books.db', books)
'''
1.http://www.naver.com 요청 -> 응답 데이터는 한글
    : 한글을 출력하기 위한 인코딩 설정값은?
        utf-8/cp949/euc-kr

2.http://www.yahoo.com 요청 -> 응답 데이터는 영문
    영어를 출력하기 위한 인코딩 설정 값은?
    :utf-8/en....
'''

#로직 - 미완성
def fetch(url):
    """
    매개변수로 전달받을 url을 기반으로 웹 페이지를 추출
    웹 페이지의 인코딩 형식은 Content-Type 헤더를 기반으로 추출
    반환값: str 자료형의 HTML
    """
    f = urlopen(url)
    # HTTP 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj="utf-8")
    print("### 1. 인코딩 정보 : ", encoding)
    
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩
    html = f.read().decode(encoding)
    print("### 2. 모든 문서 내용 추출 ", html)
    return html

    

#로직 - 미완성
def scrape(html):
    """
    매개변수 html로 받은 HTML 문서의 내용을 정규 표현식을 사용해서 도서 정보를 추출
    반환값: 도서(dict) 리스트
    """
    books = []
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):

        print(partial_html)
    
        url = re.search(r'<a href="(.*?)">',partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        print("###3. 추출한 url 데이터 : " + url) #http://www.hanbit.co.kr
        # 태그를 제거해서 도서의 제목을 추출
        title = re.sub(r'<.*?>','', partial_html)
        print("###4. title : ", title)
        books.append({'url': url, 'title' : title })
    return books

#로직 - 미완성
'''
추출할 데이터 일부 예시
url : http://www.hanbit.co.kr/store/books/look.php?p_code=B7198274060
title :  재미있고 빠른 한글 1권 : 기본 모음과 자음
'''
def save(db_path, books):
    """
    매개변수 books로 전달된 도서 목록을 SQLite 데이터베이스에 저장
    데이터베이스의 경로는 매개변수 db_path로 지정
    반환값: None(없음)
    """
    conn = sqlite3.connect(db_path)
    #커서를 추출
    c = conn.cursor()
    
    # execute() : 메서드로 SQL을 실행
    # 스크립트를 여러 번 실행 할 수 있으므로 기존의 books 테이블을 제거
    c.execute('DROP TABLE IF EXISTS books')

    #books 테이블을 생성
    c.execute('''
        CREATE TABLE books (
             title text,
             url text
        )
    ''')
    
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()