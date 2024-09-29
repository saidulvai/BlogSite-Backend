from django.contrib import admin
from .models import Category, Blogs,Rating

admin.site.register(Blogs)
admin.site.register(Rating)

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
