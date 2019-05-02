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
torrentLink = links[torrentIndex]['href']
uploadResponse = requests.post(
   'https://www.seedr.cc/oauth_test/resource.php',
    data = {'torrent_magnet':torrentLink,'func':'add_torrent','access_token':'673446456f8ebc3f9196d87d18643936a372a339'}
)
user_torrent_id = uploadResponse.json()['user_torrent_id']
loading = True
while loading:
    foldersResponse = requests.post(
        'https://www.seedr.cc/api/folders',
        data={'access_token':'673446456f8ebc3f9196d87d18643936a372a339'}
    )
    torrents = foldersResponse.json()['torrents']
    loading = False
    for torrent in torrents:
        if torrent['id'] == user_torrent_id:
            print("loading ",torrent['progress']," %")
            loading = True
print("finished")
folders = requests.post(
        'https://www.seedr.cc/api/folders',
        data={'access_token':'673446456f8ebc3f9196d87d18643936a372a339'}
    ).json()['folders']
count = 1
for folder in folders:
    print(count,folder['name'])
folderIndex = int(input("Enter a folder number to download: ")) - 1
folder = folders[folderIndex]
archive_arr = [{"type":"folder","id":folder['id']}]
create_empty_archive_response = requests.post(
    'https://www.seedr.cc/oauth_test/resource.php',
    data = {'access_token':'673446456f8ebc3f9196d87d18643936a372a339','archive_arr':archive_arr,'func':'create_empty_archive'}
)
archive_id = create_empty_archive_response.json()['archive_id']
print(create_empty_archive_response.json())
fetch_archive_response = requests.post(
    'https://www.seedr.cc/oauth_test/resource.php',
    data = {'access_token':'673446456f8ebc3f9196d87d18643936a372a339','archive_id':archive_id,'func':'fetch_archive'}
)
print(fetch_archive_response.json())
# requests.post(
#     'https://www.seedr.cc/oauth_test/resource.php',
#     data = {'access_token':'673446456f8ebc3f9196d87d18643936a372a339','delete_arr':archive_arr,'func':'delete'}
# )
# print(url) 
