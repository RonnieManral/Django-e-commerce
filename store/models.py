from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

        
class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE , default=1)
    desc = models.CharField(max_length=200,default="")
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField()
    update_on = models.DateTimeField()

    def __str__(self):
        return str(self.product)
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=40)
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    

    

    


    



