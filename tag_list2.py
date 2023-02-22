# This program is to retreive all descendants
# of the body tag from a given web page

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')
print("\nDescendants of the body tag(python.org):\n")
root = soup.html
child = [e.name for e in root.descendants if e.name is not None]
print(child)