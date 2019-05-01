import requests,sys
from bs4 import BeautifulSoup
movieRulzResponse = requests.get(
    'https://2movierulz.ms/',
    params={'s' : sys.argv[1]}
)
soup = BeautifulSoup(movieRulzResponse.content, 'html.parser')
mydivs = soup.findAll("div", {"class": "featured"})
a  = mydivs[0].findChildren("div", {"class": "cont_display"} , recursive=True)
for i in a:
    print(i.find("a")['title'])
