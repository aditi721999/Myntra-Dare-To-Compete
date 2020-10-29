#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:31:57 2020

@author: aadi
"""

import pandas as pd
import urllib.request

data=pd.read_csv('run_results.csv')
count=1

for i in data['selection1_image']:
     path="photo_"+str(count)+".jpg"
     urllib.request.urlretrieve(i,path)
     count=count+1
     print(path)