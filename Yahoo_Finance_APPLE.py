# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:21:18 2020

@author: thana
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


r=requests.get("https://uk.finance.yahoo.com/quote/AAPL/history?p=AAPL", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"Pb(10px) Ovx(a) W(100%)"})


ll=[]

for item in all:  
     
    for column_group in item.find_all("table",{"class":"W(100%) M(0)"}):
        #print(column_group)
        
        for feature_group in column_group.find_all("tr",{"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"}):
            #print(feature_group.find("td",{"class":"Py(10px) Ta(start) Pend(10px)"}).text)
            dd={}
            dd["Date"]=feature_group.find("td",{"class":"Py(10px) Ta(start) Pend(10px)"}).text
            try:
                dd["Open Price"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[0].text
            except:
                dd["Open Price"]=None
            try:
                dd["High Price"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[1].text
            except:
                dd["High Price"]=None
            try:
                dd["Low Price"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[2].text
            except:
                dd["Low Price"]=None
            try:
                dd["Close Price"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[3].text
            except:
                dd["Close Price"]=None
            try:
                dd["Adj. Close Price"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[4].text
            except:
                dd["Adj. Close Price"]=None
            try:
                dd["Volume"]=feature_group.find_all("td",{"Py(10px) Pstart(10px)"})[5].text
            except:
                dd["Volume"]=None
            ll.append(dd)

df=pd.DataFrame(ll)
df = df[['Date','Open Price','High Price', 'Low Price','Close Price','Adj. Close Price','Volume']]
df.to_csv("Apple_Stock_Prices.csv")
        





