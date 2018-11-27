# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 17:13:09 2018

@author: Playdata
"""

import pandas as pd
import re
import json
import sys
import os
import numpy as np
import csv

def replace(text):
    try:
        return text.strip().replace(',','')
    except AttributeError:
        return text

def make_int(text):
    try: 
        return (text.replace('','0'))
    except AttributeError:
        return text



# pandas version
data = pd.read_table("(2017.05).csv",encoding = 'CP949',sep=r',',names = ['지역구분' ,'대상 가구수(호)' ,'가구당 평균 전력사용량(kWh)','가구당 평균 전기요금(원)'],
                     converters ={'대상 가구수(호)':replace,'가구당 평균 전력사용량(kWh)':replace,'가구당 평균 전기요금(원)':replace})
print(data.info())
print(data.describe())
print(data)
data1 = data.iloc[1:18]
print(data1)
data1 =make_int(data1)

print('Pandas vesrion',data1['가구당 평균 전력사용량(kWh)'].astype(int).mean())
print('Pandas vesrion',data1['가구당 평균 전기요금(원)'].astype(int).sum())

data = pd.read_csv("(2017.05).csv",encoding = 'CP949',header=0)

# JSON version
list1 = []
def Read():
    with open("(2017.05).csv","r",encoding="CP949") as f:
          return [row for row in csv.reader(f) if row]
    
    
def Sum_result(data):   
    Sum = 0
    for line in data:
        try: Sum += int(line[i+1].strip().replace(",","")) 
        except ValueError : pass
    return Sum

def mean_result(data):   
    count = 0
    Sum = 0
    for line in data:
        try: 
            Sum += int(line[i+1].strip().replace(",",""))
            count +=1
        except ValueError : pass
 
    return Sum/count

    
if __name__ == "__main__":
    data = Read()
    for i in range(3):
         print("Mission {} value".format(i+1))
         print(mean_result(data))
         print(Sum_result(data))