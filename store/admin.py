from django.contrib import admin
from store.models import Product
from store.models import Category
from store.models import Cart
from store.models import Profile
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Profile)

