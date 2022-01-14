from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from bs4 import BeautifulSoup
import requests

def index(request):
  page = requests.get("https://tipidpc.com/catalog.php?cat=4&sec=s&page=1")
  soup = BeautifulSoup(page.content, 'html.parser')
  listItems = soup.select('#item-search-results > li table a')

  for item in listItems:
    print(item.get_text())
    print(item['href'])

  nextButton = soup.select(".pager input[value='Next']")
  return HttpResponse(nextButton)

def create(request):
  listing = Listing.objects.create(
    url = 'lol',
    name = 'lol',
    price = 12,
  )
  return HttpResponse('create')