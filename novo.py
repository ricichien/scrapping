import pandas
import requests
from bs4 import BeautifulSoup

html = ''
url = 'http://brickset.com/sets/year-2023'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

kits_list = []
for item in soup.find_all('article', attrs={'class': 'set'}):
    details = {
        'title': item.find('h1').text,
        'imagem' : item.find('img')['src'],
        'partial_link': item.find('div' , attrs={'class' : 'meta'}).find('a')['href']
    }
    kits_list.append(details)

pip install openpyxl

df_kits = pandas.DataFrame.from_dict(kits_list)
df_kits.to_excel('./dados.xlsx')
