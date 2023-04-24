from django.contrib import admin

# Register your models here.
from blog.models import Post, Trainer

#admin.site.register(Post)
# admin.site.register(Trainer)

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title','date_created','date_updated','author']
    prepopulated_fields = {"slug":("title",)}


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name','info','image']
