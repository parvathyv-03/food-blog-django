from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media',blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    

    def __str__(self):

        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'