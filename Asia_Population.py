#!/usr/bin/env python
# coding: utf-8

from gazpacho import get, Soup
import pandas as pd

base_url = "https://www.countryaah.com/asian-countries/"

html = get(base_url)

soup = Soup(html)

table = Soup(soup.find("table").html)


len(table.find("tr"))

data = {}
for i in range(1,len(table.find("tr"))):
    data[table.find("tr")[i].find("a")[1].text] = table.find("tr")[i].find("td")[5].text
               
my_data = {'countries' : list(data.keys()), 'Population' : list(data.values())}

df = pd.DataFrame.from_dict(my_data,orient='columns')
df['Population'] = df['Population'].str.replace(",","")
df['Population'] = df['Population'].astype(int)
df = df.sort_values(by='Population', ascending = False)

print(df)
