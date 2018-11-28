import urllib2
from bs4 import BeautifulSoup
import json

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns"
html= urllib2.urlopen(url)
soup= BeautifulSoup(html, "lxml")



#scrape player data
data_rows= soup.find_all(class_= {'row1', 'row2'})

#scrape the columns
for column in data_rows[:20]:
    try:
        athlete= column.contents[0].getText()
        pos= column.contents[1].getText()
        td= column.contents[6].getText()
        team= column.contents[2].getText()
        tdplayers= (athlete, pos, td, team)
        print json.dumps(tdplayers)

    except:
        print 'Nope'

