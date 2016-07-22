from django.contrib import admin
from .models import Album, Photo, Post

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 10

class AlbumModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
    (None, {'fields': ['title', 'slug']}),
    ]
    inlines = [PhotoInline]
    list_display= ["title"]
    list_display_links = ["title"]

    class Meta:
        model = Album

class PostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display= ["title", "published_date", "updated"]
    list_display_links = ["published_date"]
    list_filter = ["title", "updated"]
    search_fields = ["title", "content"]
    list_editable = ["title"]
    class Meta:
        model = Post


admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Post, PostModelAdmin)
