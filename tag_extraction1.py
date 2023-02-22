# This program is to remove a tag from a
# given tree of HTML document

from bs4 import BeautifulSoup
html_doc = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_doc,'lxml')

print("Original Markup: ")
a_tag = soup.a 
print(a_tag)

new_tag = soup.a.decompose()
print("\nAfter decomposing: ",new_tag)