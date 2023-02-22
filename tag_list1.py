# This program is  to retreive children of the HTML
# tag from a given web page

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')
print("\nChildren of the HTML tage(python.org):\n")
root = soup.html
child = [e.name for e in root.children if e.name is not None]
print(child)