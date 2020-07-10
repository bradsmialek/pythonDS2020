#!/usr/bin/python3
import requests
import pprint
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4)

r=requests.get("https://fabpedigree.com/james/mathmen.htm")

c = r.content

#pp.pprint(c)

soup=BeautifulSoup(c, "html.parser")
#print(soup.get_text())
#print(soup.prettify())

names=[]
for a in soup.find_all("tr"):
   print(a.get_text())
   text=a.get_text
   names.append(text)

pp.pprint(text)
