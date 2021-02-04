class SP500:
    def __init__(self):
        self.url = None #"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def getting_comps_2(self, url):
        import requests
        response = requests.get(url)






        wikipediafile = response.text
        splitwikipediafile = wikipediafile.split("<th>Founded")
        secondwikisplit = splitwikipediafile[1].split("Selected_changes_to_the_list_of_S.26P_500_components")

        data = {"Company":[]}


        wikilist = secondwikisplit[0].split("href=")
        #print(len(wikilist))
        start = 1
        end = len(wikilist)
        #tracker = 0

        for position in range(len(wikilist)):

            #if position > start:
                #tracker = (position - (start + 1))%4
            if "nyse" in wikilist[position]:
                if "/quote" in wikilist[position]:
                    data["Company"].append((wikilist[position].split('">')[1]).split('</a>')[0])
                    #print(wikilist[position])
            if "nasdaq" in wikilist[position]:
                if "/symbol" in wikilist[position]:
                    data["Company"].append((wikilist[position].split('">')[1]).split('</a>')[0])
        return(data)
            #thirdwikisplit = wikilist[tracker] #1,5,9...
            #fourthsplit = (thirdwikisplit.split('">')[1]).split('</a>')[0]
            #print(fourthsplit)
            #tracker +=4
        #htmlfile = open("wikipedia.txt", "w+",encoding="UTF-8")

        #htmlfile.write(secondwikisplit[0])
