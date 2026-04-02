"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.shortcuts import render
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request, "about.html")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('about/',about,name='about'),
    path('blog/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('payments/',include('payments.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
