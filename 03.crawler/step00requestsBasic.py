"""
PyPI에서 제공하는 requests library를 활용한 웹 페이지 응답 정보 추출해 보기
Chrome 브라우저의 속성 f12
http://hanbit.co.kr
"""
import requests

r = requests.get('http://hanbit.co.kr')

# http 응답 상태 코드 확인
print("############################")
print(r.status_code)

# 응답에 대한 모든 헤더 정보값 확인
print("############################")
print(r.headers)


# header 정보중 content-type 정보만 확인
print("############################")
print(r.headers['content-type'])


# HTTP헤더를 기반으로 인코딩 정보 추출
print("############################")
print(r.encoding)
