import requests

page = requests.get("https://bhaskarmac.github.io/scrapper/simple.html")
print page
print page.status_code
print "=============="
print page.content
