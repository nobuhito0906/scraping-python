import requests 
from bs4 import BeautifulSoup;

response = requests.get("https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q12256314127")
soup = BeautifulSoup(response.text,'html.parser')
title = soup.find('title').get_text()
print(title)