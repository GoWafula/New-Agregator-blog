
from django.shortcuts import render,redirect
from blog.models import Article
from django.core.paginator import Paginator


# Create your views here

#Scrape ntv_kenya
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_ntv():
    url = 'https://ntvkenya.co.ke/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('li', class_ = 'single_item flex__start--row')
    for article in articles:
        title = article.find('h3', class_ = 'title').text.strip()
        link = article.find('a', class_ = 'thumb_vid')['href']

        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, "html.parser")
        author = article_soup.find('span', class_='meta-inf')
        if author is not None:
            article_author = author.text.strip()
        else:
            article_author = ''
        date_string = article_soup.find('span', class_ = 'date-vid').text.strip()
        article_date = datetime.strptime(date_string, '%B %d, %Y').date()

        if not Article.objects.filter(url=link).exists():
            article = Article(title=title, author = article_author, pub_date=article_date, url = link)
            article.save()


def scrape_k24():
    url = 'https://www.k24tv.co.ke/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', class_ = 'col-md-4 my-2')
    for article in articles:
        title = article.find('p', class_ = 'text-justified font-15 fw-500').text.strip()
        link = article.find('a')['href']

        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, "html.parser")
        article_author = article_soup.find('a', class_='author url fn').text.strip()
        date1 = article_soup.find('a',class_='author url fn').find_next('span').find_next('span').text.strip()
        date2 = date1[8:19]
        date_format = '%d %b, %Y'
        article_date = datetime.strptime(date2, date_format).date()

        if not Article.objects.filter(url=link).exists():
            article = Article(title=title, author = article_author, pub_date=article_date, url = link)
            article.save()

def home(request):
     
     # scrape data from k24
     scrape_k24()

     # scrape data from ntv
     scrape_ntv()

    

     

     articles = Article.objects.all().order_by('-pub_date')
     paginator = Paginator(articles,9)
     page = request.GET.get('page')
     articles = paginator.get_page(page)


     context = {'articles': articles}
     return render(request, 'news_list.html', context)



def about(request):
    return render(request, 'about.html')
