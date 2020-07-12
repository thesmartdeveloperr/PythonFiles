from bs4 import BeautifulSoup
import requests
url="https://dev.to/javinpaul/the-2019-web-development-frontend-backend-roadmap-4le2"
response=requests.get(url)
print(response)
data=response.text
soup=BeautifulSoup(data,'html.parser')
tags=soup.find_all('h1')
print(tags)