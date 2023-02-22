# This program is to extract all the text from
# a given web page

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')

print("TEXT FROM THE WEB PAGE: ")
print(soup.get_text())