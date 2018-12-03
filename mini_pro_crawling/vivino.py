#vivino 
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

main_url = "https://www.vivino.com/"
keyword = input("What kind of wine you want to buy??")

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
def main():
    search()

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
    
    
   
def crawler():    

    
    for i in range(1,5):
        soup = BeautifulSoup(driver.page_source, "lxml" )
        wine_items = soup.select(".wine-card__content")
        driver.find_element_by_xpath('//*[@id="next"]').click()
        driver.implicitly_wait(10)
        wine_items = soup.select(".wine-card__content")
        for wine in wine_items:
            title = wine.select(".link-color-alt-grey > .bold")[0].text.replace("\n","")
            region = wine.select(".link-color-alt-grey")[1].text
            country = wine.select(".link-color-alt-grey")[2].text
            rating = wine.select(".text-inline-block")[0].text.strip().replace(" ","")
            price = wine.select(".wine-price-value")[0].text.replace("—","0")
            
            print(title, " : name")
            print(region, " : region")
            print(country, " : country")
            print(rating, ": rating")
            print(price, ": price")
            
      
    
       
    
if __name__ == "__main__":
    search()
    crawler()
