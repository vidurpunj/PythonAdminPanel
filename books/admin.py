from django.contrib import admin

# Register your models here.
from .models import Book

# admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'description')

admin.site.register(Book, BookAdmin)