from django.contrib import admin
from .models import MyModel
from .models import Book

admin.site.register(MyModel)
admin.site.register(Book)