from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from bs4 import BeautifulSoup
import requests

def index(request):
  basePath = "https://tipidpc.com"
  i = 1

  while i < 10:
    page = requests.get(f"https://tipidpc.com/catalog.php?cat=4&sec=s&page={i}")
    soup = BeautifulSoup(page.content, 'html.parser')
    listItems = soup.select('#item-search-results > li')

    for item in listItems:
      itemText = item.get_text().split('on ')
      htmlListing = BeautifulSoup(str(item), 'html.parser')
      title = htmlListing.select('table h2')[0]

      price = float(htmlListing.select('table h3')[0].get_text().replace('P',''))
      titleText = title.get_text()
      listUrl = f"{basePath}/{title.find('a')['href']}"
      print(listUrl)
      datePosted = itemText[1]

      if not (Listing.objects.filter(url=listUrl).first()):
        listing = Listing.objects.create(
          url = listUrl,
          name = titleText,
          price = price,
        )
    i += 1

  nextButton = soup.select(".pager input[value='Next']")
  return HttpResponse(nextButton)

def create(request):
  listing = Listing.objects.create(
    url = 'lol',
    name = 'lol',
    price = 12,
  )
  return HttpResponse('create')