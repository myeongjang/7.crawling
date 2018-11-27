'''
1. 모든 지역에 거주하는 대상 가구수의 합
2. 가구당 평균 전력사용량의 총 평균
3. 가구당 평균 전기요금의 합
'''
import csv # csv를 사용하기 위한 library import

newhouse = [] #house 칼럼을 저장 할 수 있늦 리스트를 만듭니다.
newVolt = []  #전력량 칼럼을 저장 할 수 있는 리스트를 만듭니다.
newPay = []   #요금 칼럼을 저장 할 수있는 리스트를 만듭니다.
with open("(2017.05).csv", "r") as f:  # with는 따로 close를 안 써도 되는 명령어입니다. 그리고 다운 받은 파일을 열고
    csv_reader = csv.reader(f) #csv.reader로 읽습니다.
    
    
    for row in csv_reader:    # 집단 
        newhouse.append(row[1].strip().replace(",","")) # 각 행의 인덱스 두번째열([1]) 공백을 없애고 쉼표를 제거합니다.
        newVolt.append(row[2].strip().replace(",","")) # 각 행의 인덱스 세번째열([2]) 공백을 없애고 쉼표를 제거합니다.
        newPay.append(row[3].strip().replace(",","")) # 각 행의 인덱스 네번째열([3]) 공백을 없애고 쉼표를 제거합니다.


def Sum(sumList):  #합계 구하는 함수
    sum = 0        # 0으로 시작하는 값 만듭니다.
    for i in range(1,len(sumList)): #list의 길이값과 그에 해당하는 range로 for loop을 만들고 
        if(sumList[i]!=""): # 특정 인덱스 값에 해당하는 행이 값이 있으면 
            sum = int(sum + int(sumList[i])) #sum을 int화 해서 합하고
        else: #아님 넘긴다
            pass
    return (sum) #그리고 결과 값 도출


def Avg(avgObject): # 평균 구하는 함수 만들기
    count = 0 # 값 있는 애들 카운트
    for i in range(1,len(avgObject)): # 1 부터 입력한 리스트 열만큼 for loop 생성 
        if(avgObject[i]!=""): # 입력한 리스트의 행이 값이 있을때
            count +=1  #count 추가
    
    return (Sum(avgObject)/count) #평균 값 도출



print(Sum(newhouse))
print(Sum(newPay))
print(Avg(newVolt))