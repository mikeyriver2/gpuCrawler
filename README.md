Python - Django - Equivalent of https://github.com/mikeyriver2/gpuCrawler-laravel
<br />Purpose: To Test the difference in response time of laravel vs django.
<br />Function: Scrape GPU listings from tipidp
```
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
```
Django response time for 1 page (while < 2 instead of 10) ~ 100ms (1/2 the time of laravel). Surprisingly, even with saving the db, django outperforms laravel in this aspect
