from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page_view(request):
  return HttpResponse("Homepage")

def about_page_view(request):
  context = {"name":"Hari", "job":"Looking for a Job"}
  return render(request, "pages/about.html", context)