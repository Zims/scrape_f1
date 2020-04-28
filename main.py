from bs4 import BeautifulSoup
import requests

res = requests.get('https://f1.lv/2020/')
soup = BeautifulSoup(res.text, 'html.parser')
all_class = soup.select('.entry-title.td-module-title')

print(all_class[0].get('a href'))

