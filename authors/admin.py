from django.contrib import admin

# Register your models here.
from .models import Author

# admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')

admin.site.register(Author, AuthorAdmin)