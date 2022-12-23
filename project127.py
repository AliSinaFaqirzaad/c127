from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

name=[]
distance=[]
mass=[]
radius=[]

page=requests.get(bright_stars_url)
soup=bs(page.text,'html.parser')
star_table=soup.find("table")

temp_list=[]
table_row=star_table.find_all('tr')
for i in table_row:
    td=i.find_all('td')
    row=[j.text.rstrip() for j in td ]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

output=pd.DataFrame(list(zip(name,distance,mass,radius)),columns=["star_name","distance","mass","radius"])
output.to_csv("bright_stars.csv")


