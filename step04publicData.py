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
        return text.replace(',','')
    except AttributeError:
        return text

def make_int(text):
    return int(text.strip('" '))




csv_path = os.path.join("(2017.05).csv")
data = pd.read_table("(2017.05).csv",encoding = 'CP949',sep=r',',names = ['지역구분' ,'대상 가구수(호)' ,'가구당 평균 전력사용량(kWh)','가구당 평균 전기요금(원)'],
                     converters ={'가구당 평균 전기요금(원)':replace} )
print(data)
data['가구당 평균 전기요금(원)'].replace(None,0)




"""
list1 = []
with open("(2017.05).csv","r",encoding="CP949") as f:
    data = csv.reader(f)
    #print(type(data))
    #print(list(data))
    for i in list(data):
        print(i)
        for x in i:
            data1 = x.replace(',','')
            list1.append(data1)
 """           