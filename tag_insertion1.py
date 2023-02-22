# This program is insert tags or strings immediately
# before specified tags or string

from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>",'lxml')
print("\nOriginal Markup: ")
print(soup.b)

tag = soup.new_tag("i")
tag.string = ("Python")
#print(soup.b)

print("\n Newer Markup after inserting the text: ")
soup.b.string.insert_before(tag)
print(soup.b)