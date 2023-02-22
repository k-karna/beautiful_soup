# This program is to find all the h2 tags and list the
# first four from the webpage python.org 

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'html.parser') #or LXML

print("First four h2 tags from the webpage python.org")
print(soup.find_all('h2')[0:4])