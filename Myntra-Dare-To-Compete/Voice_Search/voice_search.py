#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:39:44 2020

@author: aadi
"""
import speech_recognition as sr
recog = sr.Recognizer()


sample_audio = sr.AudioFile('1.wav')
with sample_audio as audio_file:
    audio_content = recog.record(audio_file, duration=10)

s=recog.recognize_google(audio_content)
 
number = "-".join(s.split()).replace(' ','-')
print(number)
url='https://www.myntra.com/'+number
    
import webbrowser  
webbrowser.open(url, new=0, autoraise=True)