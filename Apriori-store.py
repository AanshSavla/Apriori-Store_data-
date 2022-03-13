# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:09:35 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv("D:\AanshFolder\datasets\store.csv")
print(store_data.head())
records=[]

for i in range(0,16):
    records.append([str(store_data.values[i,j]) for j in range(0,8)])
association_rules = apriori(records,min_support=0.0045,min_confidence=0.2,min_lift=3,min_length=2)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule:"+items[0]+"->"+items[1])
    
    print("Support:"+str(item[1]))
    print("Confidence:" + str(item[2][0][2]))
    print("Lift:"+str(item[2][0][3]))
    print("================================")