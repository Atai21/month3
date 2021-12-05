from django.contrib import admin
from .models import Comment

from bookingem import models



class BooksAdmin(admin.ModelAdmin):
    model = models.Books
    list_editable = ['title', 'description']
    list_display = ['id', 'title', 'description']
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_date', 'updated_date')

admin.site.register(models.Books, BooksAdmin)
