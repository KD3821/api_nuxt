from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'text', 'username', 'created_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
