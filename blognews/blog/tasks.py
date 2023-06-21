from celery import shared_task
from blog.views import scrape_ntv,scrape_k24



@shared_task
def scrape_news():
    scrape_ntv
    scrape_k24
