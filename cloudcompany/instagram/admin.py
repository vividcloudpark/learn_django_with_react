from django.contrib import admin
from django.utils.html import mark_safe
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_url', 'message', 'created_at', 'is_public', 'updated_at', 'message_length']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ["message"]

    def message_length(self, post):
        return len(post.message) 
    
    def photo_url(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style ="width:72px " />')
        return None

    message_length.short_description = "글자수"