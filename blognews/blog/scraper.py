import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://citizentv.co.ke/category/news/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    title = article.find('h3').text.strip()
    author = article.find('span', class_='byline').text.strip()
    date_str = article.find('time')['datetime']
    date = datetime.fromisoformat(date_str)
    content = article.find('div', class_='entry-content').text.strip()

    print(title)



       
