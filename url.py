# This program is to extract all the URLs
# from the webpage python.org that are nexted within <li> tags

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'html.parser')

urls = []

for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])

print(urls)