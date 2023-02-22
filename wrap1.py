# This program is to replace a given tag with whatever
# inside a given tag

from bs4 import BeautifulSoup
markup = '<a href = "https://w3resource.com/">Python exercise<i>w3resource.com</i></a>'
soup = BeautifulSoup(markup,"lxml")

a_tag  = soup.a 
print("Original markup: ")
print(a_tag)

a_tag.i.unwrap()
print("\nAfter unwrapping: ")
print(a_tag)