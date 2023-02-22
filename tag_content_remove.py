# This program is remoce the contents of a tag 
# in a given HTML document

from bs4 import BeautifulSoup
html_doc = '<a href ="https://w3resource.com/">Python <i>exercises</i></a>'
soup = BeautifulSoup(html_doc,"lxml")

print("Original Markup: ")
print(soup.a)
tag = soup.a 
tag.clear()
print("Cleaner content of tag a now: ")
print(soup.a)