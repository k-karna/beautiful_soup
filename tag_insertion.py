# This program is insert a new text within a
# URL in a specified position

from bs4 import BeautifulSoup
html_doc ='<a href="http://example.com/">HTML<i>example.com</i></a>'

soup = BeautifulSoup(html_doc,'lxml')
tag = soup.a
print("\Original Markup: ")
print(tag.contents)

tag.insert(1,"CSS") # 2-> position of the text (1,2,3..)
print("\n Newer Markup now: ")
print(tag.contents)