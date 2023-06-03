import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# getting html data fromm url
page = requests.get("https://www.carwale.com/maruti-suzuki-cars/", headers=headers)

# here the BeautifulSoup module is used to access the conent inside the scraped data
soup = BeautifulSoup(page.content, 'html.parser')   

for i in soup.find_all('li', attrs={'class': "o-fzptUA"}) : 
    print(i.find('img')['src'])
    # or
    # print(i.find('img').get("src"))


