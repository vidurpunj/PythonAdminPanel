from django.contrib import admin
from .models import MyModel
from .models import Book
from .models import Author

admin.site.register(MyModel)
admin.site.register(Book)
admin.site.register(Author)

