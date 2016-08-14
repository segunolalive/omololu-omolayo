from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

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
    album_group = models.ForeignKey('AlbumGroup', on_delete = models.CASCADE, default="unnamed")
    # album_group = models.CharField(max_length=120)

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
