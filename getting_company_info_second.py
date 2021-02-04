#from statuscodes import UrlInfo
from getting_sp500_companies_second import SP500
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from datetime import date

sp500list = SP500.getting_comps_2('self',"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
#sp500list ={'Company': ['mmm', 'gme','fkjhgjh']}
print(sp500list)

indicators ={"SYM":[],
"Previous Close":[],
"Open":[],
"Bid":[],
"Ask":[],
"Day&#x27;s Range":[],
"52 Week Range":[],
"Volume":[],
"Avg. Volume":[],
"Market Cap":[],
"Beta (5Y Monthly)":[],
"PE Ratio (TTM)":[],
"EPS (TTM)":[],
"Earnings Date":[],
"Forward Dividend &amp; Yield":[],
"Ex-Dividend Date":[],
"1y Target Est":[]	}

#x = len(indicators)
#data  = {}



for element in sp500list["Company"]:
    company = element
    print(company)
    try:
        #url ="https://finance.yahoo.com/quote/{}".format(element)
        url ="https://finance.yahoo.com/quote/{}".format(element)
        page = requests.get(url)


        soup = bs(page.content, 'html.parser')


        result =  soup.find(id = "quote-summary")

        results = result.find_all("td",class_="Ta(end)")
        list = []
        for element in results:

            #print(element.text)
            datavalue = element.text
            list.append(datavalue)
        x = 0
        for field in indicators:
            if field == "SYM":
                indicators[field].append(company)
            else:
                indicators[field].append(list[x])
                x+=1
                #indicators[field].append(datavalue)
    except:
        for field in indicators:
            if field == "SYM":
                indicators[field].append(company)
            else:
                indicators[field].append("err")
        continue
df = pd.DataFrame.from_dict(indicators)
df['asofdt'] = str(date.today())
df.to_excel("..\sp500info_{}.xlsx".format(str(date.today())),sheet_name = 'data')
print(df)
