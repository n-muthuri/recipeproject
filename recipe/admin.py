from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')  # Add image field to the list display
    search_fields = ['title', 'content']  # Search by title and content

admin.site.register(Blog, BlogAdmin)
