from django.contrib import admin

from django.contrib import admin
from rango.models import Category, Page

#regestering each class we want to include
admin.site.register(Category)
admin.site.register(Page)