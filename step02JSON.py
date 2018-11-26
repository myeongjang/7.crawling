# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:58:06 2018

@author: Playdata

이기종 간에 호환되는 포멧인 JSON 타입으로 변환하는 작업
JSON 사용 사유
   : 값 구분이 명확
   : 기기에 종속적이지 않음
   : 모든 언어가 호환되는 포맷
   : csv.
   
API
   1. python의 list를 Json 형태(객체)로 변환 : dumps()
   2. json의 데이터를 python의 데이터로 변환 : loads()
   
실습단계 
   1. 모듈 import
   2. test 데이터 구성
   3. json 객체로 변환
   
고려사항
   1. 한글 데이터 보호(인코딩)
   
"""
import json
friends = [{'f1' : 1, 'name' : '박성백'},
           {'f2' : 2, 'name' : '이이'},
           {'f3' : 3, 'name': '허준'}]
print(friends[2]['name'])
print(friends)
jsonData = json.dumps(friends, ensure_ascii=False)
print(jsonData)
print('### 타입 비교###')
print(type(friends))
print(type(jsonData))

print('### json 확장자 파일로 생성 ###')
with open("friens.json","w", encoding="utf-8-sig") as f:
    json.dump(friends, fp=f, ensure_ascii=False)
    