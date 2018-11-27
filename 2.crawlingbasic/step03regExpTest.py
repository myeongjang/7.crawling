'''

'''
import re

def reUse():
    # test data - http://www.hanbit.co.kr에서 발췌한 tag 구조
    data =  '<td class="left"><a href="/store/books/look.php?p_code=B7198274060">book info</a></td>'

    #data 변수의 데이터에서 /store/books/look.php?p_code=B7198274060  
    d1 = re.search(r'href="(.*)"',data).group(1) #'()'로 그룹화를 하고  첫번째 것을 뽑는다 
    print(d1)

    d2 = re.sub(r"<.*?>", "", data) # book info를 제외하면 전부 <> 가 포함됩니다. 그래서 book info 만 출력을 원한다면 book info를 제외한 나머지의 패터을 파악한다 
    print(d2)

    d3 = re.search(r'p_code=(.*)(")',data).group(1) #p_code로 시작점을 두고 그 뒤에
    print(d3)


if __name__ == "__main__" :
    reUse()