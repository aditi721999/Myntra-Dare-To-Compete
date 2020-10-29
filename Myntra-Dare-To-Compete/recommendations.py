#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:32:37 2020

@author: aadi
"""

list_of_questions = ['Gender :',
                    'Occasion?',
                     'Which among the following is most close to your body type?',
                     'Which among the following is most close to your skin complexion ?',
                     'Any preferred color ?',
                     'Any preferred category?'
                     
                     ]

lists_of_answers = [['A:Woman','B:Man'],
                    ['A:Casual Wear', 'B:Party Wear', 'C:Festive Wear'],
                    ['A:Triangle', 'B:Inverted Triangle', 'C:Rectangle', 'D: Prefer Not To Answer'],
                    ['A:Dark Brown', 'B:Medium Brown',  'C:Light Brown', 'D:Prefer Not To Answer'],
                    ['A:None ', 'B:White ', 'C:Navy-Blue ', 'D:Red ','E:Blue ','F:Lavender','G:Purple ','H:Green ','I:Teal ','J:Orange ','K:Black ' ],
                    ['A:None', 'B:Kurta-Sets/Suits', 'C:Kurtas', 'D:Shirt/Top','E:Jeans']]



def questions():
    print('Welcome , I am your personal assistant for today')
    print('Please answer few of my questions')
    count=1
    occasion=''
    occ=''
    gender=''
    color=''
    category=''
    c=''
    gen=''
    url1=''
    for each_question, each_answer in zip(list_of_questions, lists_of_answers):
        print(each_question + '\n' + ' '.join(each_answer))
        get_answer = input()
        if count==1:
            gen=get_answer
            if get_answer=='A':
                gender='Gender%3Amen%20women%2Cwomen'
            if get_answer=='B':
                gender='Gender%3Amen%2Cmen'
        if count==2:
            occ=get_answer
            if get_answer=='A':
                occasion='casual-wear?'
            if get_answer=='B':
                occasion='party-wear?'
            if get_answer=='C':
                occasion='festive-wear?'
        if count==3:
            category=get_answer
            if get_answer=='C':
               url1='https://www.myntra.com/belt?'
            if get_answer=='B':
               url1='https://www.myntra.com/boots?'
            if get_answer=='A':
               url1='https://www.myntra.com/long-coat?'
            
        if count==4:
            if get_answer=='A':
                color='Color%3ABlack_36454f%2COlive_3D9970%2CPeach_ffe5b4%2CPurple_800080'
            if get_answer=='B':
                color='Color%3AOrange_f28d20%2CRose_dd2f86%2CTeal_008080%2CWhite_f2f2f2'
            if get_answer=='C':
                color='Color%3ABlue_0074D9%2CLavender_d6d6e5%2CPink_f1a9c4%2CRed_d34b56'
           
        if count==5:
            if get_answer=='K':
                color='Color%3ABlack_36454f'
            if get_answer=='B':
                color='Color%3AWhite_f2f2f2'
            if get_answer=='C':
                color='Color%3ANavy Blue_3c4477'
            if get_answer=='D':
                color='Color%3ARed_d34b56'
            if get_answer=='E':
                color='Color%3ABlue_0074D9'
            if get_answer=='F':
                color='Color%3ALavender_d6d6e5'
            if get_answer=='G':
                color='Color%3APurple_800080'
            if get_answer=='H':
                color='Color%3AGreen_5eb160'
            if get_answer=='I':
                color='Color%3ATeal_008080'
            if get_answer=='J':
                color='Color%3AOrange_f28d20'
            
            
        if count==6:
            temp = get_answer
            get_answer = category
            category = temp
            if get_answer=='A':
               if category=='A':
                  if occ!='C' and gen=='B':
                     c='Categories%3ANehru%20Jackets'
                  else:
                     c='Categories%3AKurtas'
               if category=='B':
                  if occ!='C' and gen=='B':
                     c='Categories%3ANehru%20Jackets'
                  else:
                     c='Categories%3AKurta Sets'
               if category=='C':
                  if occ!='C' and gen=='B':
                     c='Categories%3ANehru%20Jackets'
                  else:
                     c='Categories%3AKurtas'
               if category=='D':
                  if gen=='B':
                     c='Categories%3AShirts%3A%3APattern%3AChecked'
                  else: 
                     if occ=='C':
                        c='Categories%3ASaree%20Blouse'
                     else:
                        c='Categories%3ATops%3A%3ASleeve'
               if category=='E':
                  if occ=='C':
                     occasion='jeans?'
                     c=''
                  else:
                     c='Categories%3AJeans%3A%3AFit%3ABootcut'
                
                
            if get_answer=='B':
               if category=='A':
                  if occ!='C' and gen=='B':
                     c='Categories%3ABlazers'
                  else:
                     c='Categories%3AKurtas%3A%3ANeck%3AV-Neck'
               if category=='B':
                  if gen=='B':
                     occasion='kurta Sets?'
                     c=''
                  else:
                      c='Categories%3AKurta Sets%3A%3ATop Shape%3AAnarkali'
               if category=='C':
                  if occ!='C' and gen=='B':
                     occasion='kurtas?'
                     c=''
                  else:
                     c='Categories%3AKurtas%3A%3ANeck%3AV-Neck'
               if category=='D':
                  if gen=='B':
                     c='Categories%3AShirts%3A%3AFit%3ASkinny%20Fit%2CSlim%20Fit'
                  else:
                     if occ=='C':
                        c='Categories%3ASaree%20Blouse'
                     else:
                        c='Categories%3ATops%3A%3AType%3APeplum%2CWrap'
               if category=='E':
                  if occ=='C':
                     occasion='jeans?'
                     c=''
                  else:
                     c='Categories%3AJeans%3A%3AWaist Rise%3AHigh-Rise'
             
            if get_answer=='C':
               if category=='A':
                  if occ!='A' :
                     c='Categories%3ASweatshirts'
                  else:
                     c='Categories%3AJeans%3A%3AFit%3ABoyfriend Fit%2CStraight Fit'
               if category=='B':
                  if gen=='A':
                     c='Categories%3AKurta Sets%3A%3ATop Shape%3AAnarkali'
                  else:
                     occasion='Kurta Sets?'
                     c=''
               if category=='C':
                  if occ!='C' and gen=='B':
                     occasion='?'
                     c=''
                  else:
                     c='Categories%3AKurtas%3A%3ANeck%3ARound Neck%2CShirt Collar%2CV-Neck'
               if category=='D':
                  if gen=='A':
                     if occ=='C':
                        c='Categories%3ASaree%20Blouse'
                     else:
                        c='Categories%3ATops%3A%3ANeck%3AScoop Neck'
                  else:
                     c='Categories%3AShirts%3A%3APattern%3AStriped'
               if category=='E':
                  if occ=='C':
                     occasion='jeans?'
                     c=''
                  else:
                     c='Categories%3AJeans%3A%3AFit%3ABoyfriend Fit%2CStraight Fit'
                
   
        
        count=count+1;        
     
    print('THANK YOU FOR YOUR PATIENCE')
    print('Here are your customized suggestions :')
    import webbrowser
    if url1!='':
       if gen!='':
          url1=url1+'f='+gender
       webbrowser.open(url1, new=0, autoraise=True)
    if c=='' and color=='':
       url='https://www.myntra.com/'+occasion+'f='+gender
    elif c=='':
       url='https://www.myntra.com/'+occasion+'f='+color+'%3A%3A'+gender
    elif color=='':
       url='https://www.myntra.com/'+occasion+'f='+c+'%3A%3A'+gender
    else:
       url='https://www.myntra.com/'+occasion+'f='+c+'%3A%3A'+color+'%3A%3A'+gender
    
    
    webbrowser.open(url, new=0, autoraise=True)
    
       
    
if __name__ == '__main__':
    questions()
 
  
    
#s='green pink lehega choli festive'    
#number = "-".join(s.split()).replace(' ','-')
#print(number)
#url='https://www.myntra.com/'+number
#    
#import webbrowser  
#webbrowser.open(url, new=0, autoraise=True)
