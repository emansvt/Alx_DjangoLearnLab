from django.contrib import admin
<<<<<<< HEAD
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')
    ordering = ('-published_date',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'author')
    search_fields = ('content',)
    ordering = ('-created_at',)
=======

# Register your models here.
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
