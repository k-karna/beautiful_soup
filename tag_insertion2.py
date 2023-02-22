# This program is to insert tags or string immediately
# after specified tags or string

from bs4 import BeautifulSoup
soup = BeautifulSoup("<i>w3resource.com</i>","lxml")
print("Original Markup: ")

print(soup.i)
tag = soup.new_tag("b")
tag.string = ("Python")
print("\n Markup after new insertion: ")
soup.i.string.insert_after(tag)
print(soup.i)