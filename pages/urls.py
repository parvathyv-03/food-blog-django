from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('articles/',include('articles.urls')),
    path('about/',views.about,name='about'),
    path('', views.homepage,name='home'),
]
    
