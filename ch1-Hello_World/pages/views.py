# What to do when a user opens a URL
# views.py	is	where	we	handle	the	request/response logic	for	our	web	app
from django.http import HttpResponse

def home_page_view(request):
  return HttpResponse("Hello, World!")
