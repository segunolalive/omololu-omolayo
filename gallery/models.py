from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

from lolu import settings

import os.path

# Create your models here.


class Link(models.Model):
    url = models.URLField()
    short_decription = models.CharField(max_length = 120)

    def __str__(self):
        return self.url
    def __unicode__(self):
        return self.url

# background
class Background(models.Model):
    image = models.ImageField()

    def save(self):
        if Background.objects.all():
            old_background = Background.objects.get()
            old_background.delete()
        project_root = settings.BASE_DIR
        media_location = '/media_cdn/background_for_homepage.jpg'
        background_url = project_root + media_location
        if(os.path.exists(background_url)):
            os.remove(background_url)
        self.image.name = 'background_for_homepage.jpg'
        super(Background, self).save()

    def __str__(self):
        return self.image.name
    def __unicode__(self):
        return self.image.name

#gallery models here
class AlbumGroup(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    album_group = models.ForeignKey('AlbumGroup', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField()
    album = models.ForeignKey('Album', on_delete = models.CASCADE)

    def __str__(self):
        return self.image.name
    def __unicode__(self):
        return self.image.name

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Album.objects.filter(slug=slug).order_by("title")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Album)
