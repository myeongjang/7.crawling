#vivino 
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient

from selenium.webdriver.support.ui import WebDriverWait

main_url = "https://www.vivino.com/"
keyword = input("What kind of wine you want to buy??")

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)

client = MongoClient('localhost', 27017)
db = client.project
collection = db.crawling


def main():
    
    search()
    wine_crawler()

def search():
    driver.get(main_url)
    driver.implicitly_wait(10)
    time.sleep(3)
    try:
        elem = driver.find_element_by_class_name("searchBar__searchInput--2aCeZ")
        elem.clear()
        elem.send_keys(keyword)
        elem.submit() 
        
       
    except AttributeError:
        print("You searched wrong thing")
    
    
dict1={}   
def wine_crawler():    

    try:
        

        for i in range(1,5):
            soup = BeautifulSoup(driver.page_source, "lxml" )
            
            driver.find_element_by_xpath('//*[@id="next"]').click()
            driver.implicitly_wait(10)
            wine_items = soup.select(".default-wine-card")
            for wine in wine_items:
                img_ex = wine.find("figure")['style']
                img = re.findall("[/][/].+g",img_ex)
                url = wine.find('a')['href']
                title = wine.select(".link-color-alt-grey > .bold")[0].text.replace("\n","")
                region = wine.select(".link-color-alt-grey")[1].text
                country = wine.select(".link-color-alt-grey")[2].text
                rating = wine.select(".text-inline-block")[0].text.strip().replace(" ","")
                price = wine.select(".wine-price-value")[0].text.replace("—","0")
                url = main_url+url
                wineInfo = {
                    'ImageURL' : "https:"+img[0],
                    'URL' : url,
                    'Name' : title,
                    'Origin' : country,
                    'Rate' : rating,
                    'Price' : price 
                }

                collection.insert_one(wineInfo)

                print("https:"+img[0], " : img")
                print(main_url+url, " : url" )
                print(title, " : name")
                print(region, " : region")
                print(country, " : country")
                print(rating, ": rating")
                print(price, ": price")
    except Exception as e:
       print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()   
            
if __name__ == "__main__":
    main()
