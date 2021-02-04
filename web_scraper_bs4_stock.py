import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.yahoo.com/quote/MMM"

page = requests.get(url)


soup = bs(page.content, 'html.parser')


result =  soup.find(id = "quote-summary")

results = result.find_all("td",class_="Ta(end)")

for element in results:

    #print(element.attrs[])
    print(element.text)

#print(results)
#print(site.content)

#htmtextfile = open("html.txt","w+", encoding="utf-8")
#htmtextfile.write(str(site.content))
