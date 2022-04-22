import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.worldometers.info/coronavirus/#countries'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
data = []
table = soup.find(id='main_table_countries_today')
tableBody = table.find('tbody')
rows = tableBody.find_all('tr')

for row in rows:
    columns = row.find_all('td')
    columns = [i.text.strip() for i in columns]
    data.append([j if j else '/' for j in columns ])

output = open('/home/jeja/Desktop/projects/corona_table.csv', 'w')
writer = csv.writer(output)
writer.writerows(data)