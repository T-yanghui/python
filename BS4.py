from urllib.request import urlopen
from bs4 import BeautifulSoup
html  = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
print(html.geturl())
print('headers:',html.getheaders())
print('status:',html.status)
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.title)
