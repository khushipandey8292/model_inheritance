from django.contrib import admin
from .models import Page,Like,Post
# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cate','page_publish_date','user']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cate','page_publish_date','user','likes']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['post_title','post_cate','post_publish_date','user']