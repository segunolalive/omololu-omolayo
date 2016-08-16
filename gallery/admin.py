from django.contrib import admin
from .models import Album, Photo, AlbumGroup, Background, Link

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 10


class AlbumInline(admin.TabularInline):
    model = Album
    extra =3


class AlbumModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
    (None, {'fields': ['title', 'slug','album_group']}),
    ]
    inlines = [PhotoInline]

    list_display= ("title",)
    list_display_links = ["title"]

    class Meta:
        model = Album

class AlbumGroupModelAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    fieldsets = [
    (None, {'fields': ['name',]}),
    ]

    class Meta:
        model = AlbumGroup

admin.site.register(Album, AlbumModelAdmin)
admin.site.register(AlbumGroup, AlbumGroupModelAdmin)
admin.site.register(Background)
admin.site.register(Link)
