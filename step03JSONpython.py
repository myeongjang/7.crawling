# -*- coding: utf-8 -*-
'''
Created on Mon Nov 26 15:17:13 2018

@author: Playdata


1. http://www.w3schools.com 예제
- https://www.w3schools.com/python/python_json.asp

2. 예제 이해하기

3. 이 데이터를 파일로 저장
    - save()
4. 저장된 파일을 다시 read해서 python 데이터로 변환 후 활용(출력)
    - view()

5. 의도
    - json과 python의 호환 작업 익숙해지기
    - 개별 함수로 개발해서 모듈화 시키는 연습
    - main 사용 필수 : 최상위 실행 스크립트
'''
import json

data = [{
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
},
{
    "name": "Jacob",
    "age" : 24,
    "married": False,
    "divorced" : False,
    "children" : None,
    "pets" : None,
    "cars" : [
        {"model": "BMW","mpg": 28.5}
    ]
}
]
print(json.dumps(x))
def save():
    with open("data.json","w",encoding="utf-8-sig") as f:
        #list 데이터를 파일에 json 형태의 문자열로 출력
        json.dump(x, fp=f, ensure_ascii=True)
def view():
    with open("data.json","r",encoding="utf-8-sig") as f:
        #data = f.read()
        #print("##1. read() 함수로 read한 데이터 타입 ##", type(data))

        data = json.loads(data)

        print("##2. json.loads() 함수로 변환 후의 타입 ##", type(data))

if __name__ == "__main__":
    save()
    view()