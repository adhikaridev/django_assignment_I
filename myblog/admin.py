from django.contrib import admin
from .models import Author, Blog


admin.site.site_header = 'My Blog'
admin.site.site_title = 'My Blog'
admin.site.index_title = 'My Blog'
admin.site.register(Author)
admin.site.register(Blog)
