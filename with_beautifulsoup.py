import requests
from bs4 import BeautifulSoup

page = requests.get("https://bhaskarmac.github.io/scrapper/simple.html")
print page
print page.status_code

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
