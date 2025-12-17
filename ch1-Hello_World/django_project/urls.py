"""
URL configuration for django_project project.

Which URL goes to which function (view)
urls.py maps URLs → views

urls.py	tells	Django	which	pages	to	build	in	response	to	a	browser	or	URL
request.

Example:

/login/   → login page
/about/   → about page

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include #new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")), #new
]
