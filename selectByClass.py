from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("span",{"class":"green"})
print("=========",len(nameList),"==========")
for name in nameList:
    print(name.get_text())
