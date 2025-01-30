from django.contrib import admin
from .models import listings

# Register your models here.


admin.site.register(listings)

search_fields = ['title', 'category', 'price']