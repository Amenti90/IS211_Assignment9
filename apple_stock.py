from bs4 import BeautifulSoup
import json
import urllib2

url= "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
html= urllib2.urlopen(url)
soup= BeautifulSoup(html, "lxml")

page_rows= soup.find_all('tr')

for column in page_rows:
    try:
        date= column.contents[0].getText()
        close= column.contents[4].getText()
        stock_info= (date, close)
        print json.dumps(stock_info)

    except:
        print 'Nope'






