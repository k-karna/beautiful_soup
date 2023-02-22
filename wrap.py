# This program is to wrap an element in the specified tag and 
# create new wrapper

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Python exercises.</p>","lxml")
print("Original Markup: ") 
print(soup.p.string.wrap(soup.new_tag("i"))) #wraps a new tag on both side of string 

print("\n New Markup: ")

print(soup.p.wrap(soup.new_tag("div"))) 