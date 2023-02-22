# This program is to retrieve the HTML code
# of the title, its text and the HTML code of its parent

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')
print("Title:")
print(soup.title)
print("Title text:\n")
print(soup.title.text)
print("Parent content of the title:\n")
print(soup.title.parent)