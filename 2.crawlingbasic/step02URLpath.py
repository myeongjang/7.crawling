'''
절대 경로와 상대 경로 url 관리하는 연습
'''

#urllib - package명
#parse - 파일명(모듈명)
#urljoin - parse.py 내부에 내장된 urljoin 함수
from urllib.parse import urljoin

#http: client와 server간의 웹상의 통신 규약
#example.com : domainrkq, com(회사), co.kr(한국에서만 사용함을 의미)
#html : 실행 소스가 내장된 폴더명
#a.html : 해당 사이트의 html 폴더 내부에 저장된 html

base = "http://example.com/html/a.html"

#b.html은 a.html와 같은 폴더에 저장?
print(urljoin(base, "b.html")) #http://example.com/html/b.html

print(urljoin(base, "/b.html")) #http://example.com/b.html

print(urljoin(base, "../b.html")) #http://example.com/b.html

print(urljoin(base, "../img/b.html")) #http://example.com/img/b.html

print(urljoin(base, "../../css/cssView.css")) #http://example.com/css/cssView.css

print(urljoin(base, "/../../css/cssView.css"))