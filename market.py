from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq

url = "http://www.ngtradeonline.com/Home/dailypricelist?extension=txt"
page_html = uReq(url)
page_html2 = page_html.read()
page_html.close()
page_soup = Soup(page_html2, "html.parser")

stockmkt = page_soup.findAll("tbody")
mkt = stockmkt[0]
rowmkt = mkt.findAll("tr")

for row in rowmkt:
    print(row.text)
