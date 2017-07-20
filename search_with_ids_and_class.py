import requests
from bs4 import BeautifulSoup

page = requests.get("https://bhaskarmac.github.io/scrapper/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')


print "Find by class=>"
print soup.find_all(class_="outer-text")
print "==============================="
print "Find by id=>"
print soup.find_all(id="first")