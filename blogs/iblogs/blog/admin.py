from django.contrib import admin

# Register your models here.
from .models import Category, Post

# for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_image_tag", "title", "description", "url", "add_date")
    search_fields = ("title", )

class PostAdmin(admin.ModelAdmin):
    list_display = ("post_image_tag", "title", "content")
    search_fields = ("title", )
    list_filter = ("cat", )
    list_per_page = 50

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)