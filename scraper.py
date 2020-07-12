from bs4 import BeautifulSoup
import requests
m=requests.get("https://www.udemy.com/course/web-scraping-python-bs/learn/lecture/14878224#overview")
data=m.text
soup=BeautifulSoup(data,'html.parser')
required=soup.find_all('a')
print(required)
