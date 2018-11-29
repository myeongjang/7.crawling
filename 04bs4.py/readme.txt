1. url 
https://www.crummy.com/sorfware/BeautifulSoup/bs4/doc/
pip install beautifulSoup4

2. html/xml/분석에 굉장히 용이
3. 아나콘다에는 이미 설치, 순수 파이썬 개발 환경에선 install 필수
4. 필수 
    -html 구조는 필수 인지

5. 문서의 용도
    1.html  
        - 웹브라우저로 client에게 정보를 제공하기 위한 언어
        - presentation 언어
        - 구조 
        - 확장자
            1. html
            2. html 
    
    2.css
        - html 문서의 디자인 담당
        - 확장자 
            - css
        - 적용문법
            1. html 문서 내부에 포함해서 개발
                - 재사용 없이 해당 html 문서 내부에서만 사용
                - <style> css 코드들 </style>
            2. css 파일로 독립적으로 개발
                - 다수 재사용하기 위한 설계
                - *.css 개발 후 <link href="css 경로 및 파일명 확장자" />

            3. tag의 속성으로 적용
                <tag style="key:value" /> 등의 tag 자체에 inline 형식으로 적용