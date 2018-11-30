from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import json
def get_soup(url):
    return BeautifulSoup(urllib.request.urlopen(url),'html.parser')

query = input("Artist name : ")
query.split()
query=query.replace(' ','+')
url = 'https://www.google.com/search?rlz=1C1SQJL_koKR812KR812&tbm=isch&q='+query+'&chips=q:'+query+',g_1:painting:'   
print(url)
DIR="Pictures"

soup = get_soup(url)

ActualImages=[]
for a in soup.findall("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))
print("there are total" , len(ActualImages),"images")