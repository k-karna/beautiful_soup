# This program is to change the tags' content
# and replace with the something else

from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>example.com</i></a>'

soup = BeautifulSoup(html_doc,'html.parser')
tag = soup.a
print("\nOriginal Markup: ")
print(tag)
print("\nOriginal Markup with New text: ")
tag.string = "New Text - CSS"
print(tag)