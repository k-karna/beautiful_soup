# This program is find all the links tags and list
# the first en from the webpage python.org

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')

print("First four h2 tags from the PYTHON.ORG:")

print(soup.find_all('a')[0:4])