from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing

def index(request):
  return HttpResponse('lol')

def create(request):
  listing = Listing.objects.create(
    url = 'lol',
    name = 'lol',
    price = 12,
  )
  return HttpResponse('create')