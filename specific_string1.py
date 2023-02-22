# This program to print the elements that has a 
# specific id of a given web page

import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)

soup = BeautifulSoup(reqs.text,'lxml')
print("\nElements that has #python-network id:\n")
print(soup.select_one("#python-network"))