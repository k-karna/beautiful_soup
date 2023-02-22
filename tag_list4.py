# This program is to find and print all li
# tags of a given web page

import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)

soup = BeautifulSoup(reqs.text,'html.parser')
print("\nFind and print all Li tags:\n")
for tag in soup.find_all("li"):
    print("{0}: {1}".format(tag.name, tag.text))
