#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:11:20 2020

@author: aadi
"""

import cv2
import numpy as np
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': 'https://assets.myntassets.com/h_1440,q_90,w_1080/v1/assets/images/2272100/2018/2/19/11519021065151-Difference-of-Opinion-Men-Mustard-Printed-Round-Neck-T-shirt-1021519021064962-3.jpg',
        'size': 'auto'
    },
    headers={'X-Api-Key': 'y5XdMgNewA7Wog1ZyXTj67sK'},
)
if response.status_code == requests.codes.ok:
    with open('1.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)


min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

# Get pointer to video frames from primary device
image = cv2.imread("1.png")
imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)

cv2.imwrite("1.png", np.hstack([image,skinYCrCb]))
img = cv2.imread("1.png")
height, width = img.shape[:2]

# Cut the image in half
width_cutoff = width // 2
s1 = img[:, :width_cutoff]
s2 = img[:, width_cutoff:]




dif2 = cv2.absdiff(s1, s2)
cv2.imwrite("final3.png", dif2)

height, width = dif2.shape[:2]

# Cut the image in 1/3rd
h_cutoff = height// 3
s2 = dif2[h_cutoff:,: ]
cv2.imwrite("face2.png", s2)
