from django.db import models
from cms.extensions import PageExtension #TitleExtension
from cms.extensions.extension_pool import extension_pool


class Category(models.Model):
    category = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category
        
class CategoryExtension(PageExtension): #TitleExtension
    category = models.ForeignKey(Category)

extension_pool.register(CategoryExtension)
