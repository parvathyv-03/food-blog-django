from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=6,decimal_places=2,default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title
    
class Order(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.TextField()
    city=models.CharField(max_length=50)
    pincode=models.CharField(max_length=7)
    status=models.CharField(
        max_length=20,
        choices=[
            ('PENDING','Pending'),
            ('PAID','Paid')
        ],
        default='PENDING'
    )
    

    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
