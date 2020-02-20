from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   if request.method == 'POST':
      return HttpResponse("This is bot api(POST).")
   else:
      return HttpResponse("This is bot api(GET).")
