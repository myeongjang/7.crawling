# 데이터를 csv로 저장하기
# 실습 단계 1 - join
# 실습 단계 2 - csv 모듈 사용

#step01 
print('no,name,age')

# list의 데이터로 csv 구조로 변환
print(",".join(['1','허준','60']))
print(",".join(['2','신사임당','80']))


#step02 - csv 모듈사용 
"""
    history.csv 라는 파일에 쓰기
    csv 포멧 작성후에 new line 반영
    한글 데이터가 보유 고려
    한번에 하나의 row만 출력? 1차원 list
    한번에 다수의 row들 출력? 2차원 list 구성
"""
import csv
with open("history.csv", "w", newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)