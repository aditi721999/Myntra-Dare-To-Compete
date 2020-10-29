#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 01:03:19 2020

@author: aadi
"""
import requests
import sys
import shutil
import re
import threading
from bs4 import BeautifulSoup as soup

THREAD_COUNTER = 0
THREAD_MAX     = 5

def requesthandle( link, name ):
    global THREAD_COUNTER
    THREAD_COUNTER += 1
    try:
        r = requests.get( link, stream=True )
        if r.status_code == 200:
            r.raw.decode_content = True
            f = open( name, "wb" )
            shutil.copyfileobj(r.raw, f)
            f.close()
            print ("download")
    except Exception as error:
        print ("error")
    THREAD_COUNTER -= 1

def main():
    html = get_source( "https://www.google.com/search?q=blue+jumpsuit&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjW2fmBvtDsAhUTlEsFHRTrCvIQ_AUoAnoECAQQBA&biw=1440&bih=695" )
    tags = filter( html )
    for tag in tags:
        src = tag.get( "src" )
        if src:
            src = re.match( r"((?:https?:\/\/.*)?\/(.*\.(?:\images)))", src )
            if src:
                (link, name) = src.groups()
                if not link.startswith("http"):
                    link = "https://www.google.com/search?q=blue+jumpsuit&client=firefox-b-d&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjW2fmBvtDsAhUTlEsFHRTrCvIQ_AUoAnoECAQQBA&biw=1440&bih=695" + link
                _t = threading.Thread( target=requesthandle, args=(link, name.split("/")[-1]) )
                _t.daemon = True
                _t.start()

                while THREAD_COUNTER >= THREAD_MAX:
                    pass

    while THREAD_COUNTER > 0:
        pass


if __name__ == "__main__":
    main()