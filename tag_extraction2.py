# This program ti remove a tag or string from a
# given tree of HTML document and replace it with
# other tag or string

from bs4 import BeautifulSoup
html_doc = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_doc,"lxml")

print("Original Markup: ")
a_tag = soup.a 
print(a_tag)

new_tag  = soup.new_tag("b")
new_tag.string = "PHP"
b_tag = a_tag.i.replace_with(new_tag)
print("New Markup: ",a_tag)