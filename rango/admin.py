from django.contrib import admin

from django.contrib import admin
from rango.models import Category, Page

class pageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')


#regestering each class we want to include
admin.site.register(Category)
admin.site.register(Page, pageAdmin)


#Finally, register the PageAdmin class with Django’s admin interface.
#You should modify the line admin.site.register(Page). Change it to
#admin.site.register(Page, PageAdmin) in Rango’s admin.py file.