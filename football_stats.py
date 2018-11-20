import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import re

#create BeautifulSoup object
# html = urllib2.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns")
# bsObj = BeautifulSoup(html, 'lxml')



page= requests.get("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns")
bsObj= BeautifulSoup(page.content,"lxml")
table = bsObj.find_all('table')[0]

dfs= pd.read_html(str(table), header=0)
frame= dfs[0]
frame.columns =frame.iloc[1]
frame2= frame[2:21,[6]]



print (frame2)


# table= bsObj.find_all(class_= {'row1', 'row2'})
#
# for i in table[:20]:
#     print i




#find and findall in BS book
#pg 46 BS book, does it show how to iterate through the top 20 items on the website?

# Scrape specific contents


# store contents to list



# print the list

