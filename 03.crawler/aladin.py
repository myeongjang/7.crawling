import re
import sqlite3
import requests
import lxml.html

def main():
    session = requests.Session()
    response = session.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1')
    urls = scrape_list_page(response)
    count = 0
    for url in urls:
        response = session.get(url)
        booktitle = scrape_detail_page(response)
        print(booktitle)
        count += 1
        print(count) 
def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)    
    root.make_links_absolute(response.url)
    count = 0
    for a in root.cssselect('.ss_book_box .ss_book_list .bo3'):
        url = a.get('href')
        count += 1
        yield url
def scrape_detail_page(response):
     root = lxml.html.fromstring(response.content)
     bookInfo = {
        
        'title' :root.cssselect(".p_new_price_ph")[0].text_content(),
        'price' :root.cssselect(".p_topt01")[0].text_content()
     }
     return bookInfo
def normalize_space(s):
    return re.sub(r'\s+', ' ', s).strip()     
if __name__ == "__main__":
    main()

