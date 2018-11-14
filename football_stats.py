import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import json
import re

#create BeautifulSoup object
# html = urllib2.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns")
# bsObj = BeautifulSoup(html, 'lxml')



dfs= pd.read_html("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns", header=0)
for df in dfs:
    print (df)

# table= bsObj.find_all(class_= {'row1', 'row2'})
#
# for i in table[:20]:
#     print i




#find and findall in BS book
#pg 46 BS book, does it show how to iterate through the top 20 items on the website?

# Scrape specific contents


# store contents to list



# print the list

