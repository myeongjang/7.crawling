#step01robotsParser.py
'''
1. 크롤링 가능 여부를 소개하는 file 확인 로직
    1. 파일명 : robots.txt
    2. url상에서 직접 확인 명령어 :
       http://ip:80/robots.txt
       http://domain:80/robots.txt
2. python 관련 library
   urlib 에 robots.txt 확인 가능한 libary
       - robotparser

'''

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
'''
rp.set_url("htpp://wikibook.co.kr/robots.txt")
rp.read()
data = rp.can_fetch("mybot","http://wikibook.co.kr/")
print(data)
'''
rp.set_url("http://naver.com/robots.txt")
rp.read()
data = rp.can_fetch("mybot","http://naver.com/")
print(data)