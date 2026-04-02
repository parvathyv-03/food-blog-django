from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import JsonResponse
from django.conf import settings
import requests
from rest_framework .decorators import api_view
from rest_framework .response import Response
from .models import Article
from .serialiser import Article_serialiser
from django.http import HttpResponse


# Create your views here.
def article_list(request):
    articles =  Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article_list')
    else:
            form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})


@api_view(['GET'])
def article_serial(request):
     articles=Article.objects.all()
     serialiser=Article_serialiser(articles,many=True)

     return Response(serialiser.data)
