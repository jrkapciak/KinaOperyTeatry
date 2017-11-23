'''
Created on 1 lis 2017

@author: tomasz
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 
import time
import pandas as pd
import datetime
import time
import schedule
import json

html = urlopen("http://www.kinokika.pl")
soup = BeautifulSoup(html,"lxml")
find_program=soup.findAll("div", {"id": "program"})
movies =[]
how_long = []
days = []
dates = []
time_list = []
ignore_list = ["Pokaz przedpremierowy",">> Sprawdź repertuar do 16/11"]
findAll_movies = soup.find('div', {'id':'program'}).findAll('b')
findAll_time = soup.find('div',{'id':'program'}).findAll("small")


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))    

def getMovies():
    for m in findAll_movies:
        m_text = m.get_text()
        movies.append(m_text)
    for m in movies:
        if m in ignore_list:
            movies.remove(m)
        else:
            pass
        
def findTime():
    for t in findAll_time:
        t_text = t.get_text()
        time_list.append(t_text)
        

def getDates():
    for m in findAll_movies:
        my_text = m.findAllPrevious(name = 'h2')
        my_parent=my_text[0]
        days_text=my_parent.text
        sp=days_text.split("/")
        for word in sp:
            dd=hasNumbers(word)
            if dd==True: 
                dates.append(word)
            else:
                pass
            
def scrap():
    getMovies()
    getDates()
    findTime()
    hours=time_list[0::2]
    duration=time_list[1::2]
    del dates[33]
    del dates[34]

    a = [{'Title' : movies },{'Time' : hours }, {'Duration': duration},{'Date':dates}]

    #df = pd.DataFrame.from_dict(a, orient='index')
    #df.transpose()
    #result=df.to_json()
    return a
    #with open('kika.txt', 'w') as outfile:
        #json.dump(result, outfile)


# schedule.every(5).minutes.do(job)
# schedule.every().hour.do(job)
#schedule.every(1).day.at("10:30").do(scrap)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
 
# while True:
#     schedule.run_pending()
#     time.sleep(1)
               
