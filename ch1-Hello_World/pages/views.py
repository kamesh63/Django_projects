# What to do when a user opens a URL
from django.http import HttpResponse

def home_page_view(request):
  return HttpResponse("Hello, World!")
