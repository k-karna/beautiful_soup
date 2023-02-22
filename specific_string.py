# This program is to print content of elements
# that contain a specific string of a web page

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.python.org/'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,'lxml')

print("\nContent of elements that contain 'Python' string:\n")

str1 = soup.find_all(string = re.compile('Python'))
for txt in str1:
    print(" ".join(txt.split()))