import requests,sys
from bs4 import BeautifulSoup
search = ""
if(len(sys.argv) > 1):
    search = sys.argv[1]
movieRulzResponse = requests.get(
    'https://2movierulz.ms/',
    params={'s' : search}
)
print("exit request")
soup = BeautifulSoup(movieRulzResponse.content, 'html.parser')
mydivs = soup.findAll("div", {"class": "featured"})
a  = mydivs[0].findChildren("div", {"class": "cont_display"} , recursive=True)
count = 1
for i in a:
    print(count,i.find("a")['title'])
    count = count + 1
movieIndex = int(input("Enter a number: ")) - 1
movieUrl = a[movieIndex].findChildren("a",recursive = True)[0]['href']
movieUrlResponse = requests.get(
    movieUrl
)
moviesoup = BeautifulSoup(movieUrlResponse.content, 'html.parser')
links = moviesoup.findAll("a",{"class":"mv_button_css"})
count = 1
for i in links:
    print(count, i.text)
    count = count + 1
torrentIndex = int(input("Select a torrent : ")) - 1
