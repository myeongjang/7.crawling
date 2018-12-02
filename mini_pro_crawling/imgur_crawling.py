from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import json
def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")

user = input("user name : ")
user.split()
user=user.replace(' ','+')
url = 'https://'+user+'.imgur.com'
print(url)


soup = get_soup(url)
for a in  soup.findAll("a",href=True):
       print(a['href'])



'''
ActualImages=[]
for a in soup.findall("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))
print("there are total" , len(ActualImages),"images")
'''