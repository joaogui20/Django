from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class PostAdmin(admin.ModelAdmin, AdminVideoMixin):
    list_display = ('titulo', 'autor', 'categoria', 'post_data')
    list_display_links = ('titulo',)
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ['titulo']
    ordering = ['-post_data']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)