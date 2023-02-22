# This program is to add to a tags' content
# in a given HTML document

from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>example.com</i></a>'
soup = BeautifulSoup(html_doc,'lxml')

print("\nOriginal Markup: ")
print(soup.a)

soup.a.append("New Text - CSS")
print("\n After appending newer Markup: ")
print(soup.a)