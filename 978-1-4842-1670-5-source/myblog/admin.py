from django.contrib import admin
from cms.extensions import PageExtensionAdmin #TitleExtensionAdmin

from .models import Category, CategoryExtension

class CategoryAdmin(admin.ModelAdmin):
    pass

class CategoryExtensionAdmin(PageExtensionAdmin): #TitleExtensionAdmin
    pass

    
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryExtension, CategoryExtensionAdmin) 
