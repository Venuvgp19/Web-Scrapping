from gazpacho import get, Soup

base_url = "https://gadgets.ndtv.com/finance/gold-rate-in-india"

html = get(base_url)

soup = Soup(html)

data = soup.find("ul", {"class":"_flx _gldprcl"})

gold = {}

for i in range(len(data.find("div", {"class":"_gdcrt"}))):
    if i == 0:
        gold[data.find("div", {"class":"_gdcrt"})[i].text] = data.find("span")[i].text
    else :
        gold[data.find("div", {"class":"_gdcrt"})[i].text] = data.find("span")[i+1].text

print(gold)
