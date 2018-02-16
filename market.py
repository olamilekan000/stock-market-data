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

field_names = page_soup.findAll("thead")[0].findAll("tr")[0].findAll("th")

field_name_rows = []
values = []

# get header fields
for row in field_names:
    field_name_rows.append(row.text)

# loop through body
for row in rowmkt:
    row_object = {}
    # loop through fields
    field_columns = row.findAll("td")
    for idx, each_column in enumerate(field_columns):
        row_object[field_name_rows[idx]] = each_column.text
    values.append(row_object)

# Values is now an array of everything
print(values)
