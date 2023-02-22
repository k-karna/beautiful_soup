# This program is to extract a tag or string
# from a given tree of HTML document

from bs4 import BeautifulSoup
html_doc = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_doc,"lxml")

print("Original Markup: ")
print(soup.a)

i_tag = soup.i.extract()
print("\nExtract i tag from said HTML Markup: ")
print(i_tag)