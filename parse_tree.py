# This program is to create a parse tree into a 
# nicely formatted Unicode string, with a separate
# line for each HTML/XML tag and string

from bs4 import BeautifulSoup

str1 =  "<p>Some<b><i>HTML Code</i></b></p>"
print("original String:")
print(str1)
soup = BeautifulSoup("<p>Some<b><i>HTML Code</i></b></p>",'lxml')
print("\nFormatted Unicode String:\n")
print(soup.prettify())