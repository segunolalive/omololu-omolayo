from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone

from datetime import datetime

from .forms import ContactForm

from .models import Album, Photo, AlbumGroup
from urllib.parse import quote_plus


# Create your views here.

#gallery views
def home(request):
    albums = Album.objects.all()
    currentYear = datetime.now().year
    album_groups = AlbumGroup.objects.all()


    context = {
    "albums": albums,
    "year": currentYear,
    "album_groups": album_groups,
    }
    return render(request,"home.html", context)


def album_detail(request, slug):
    album_pictures = get_object_or_404(Album, slug= slug)
    albums = Album.objects.all()
    album_groups = AlbumGroup.objects.all()

    currentYear = datetime.now().year

    context = {"albums": albums,
               "pictures": album_pictures,
               "year": currentYear,
               "album_groups": album_groups,
               }
    return render(request,"album_detail.html", context)


# Contact views
def contact(request):
    title = 'Talk To Us'
    form = ContactForm(request.POST or None)
    currentYear = datetime.now().year
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_first_name = form.cleaned_data.get('first_name')
        form_last_name = form.cleaned_data.get('last_name')
        form_message = form.cleaned_data.get('message')

        email_subject = 'New mail from Visistor To Your Website'
        email_message = "user email address: %s \n fullname: %s %s \n message:\n %s" %(
            form_email,
            form_first_name,
            form_last_name,
            form_message
            )
        from_email = settings.EMAIL_HOST_USER
        recipient = [settings.DEFAULT_TO_EMAIL] #a list of  receipient emails

        """This method of sending mails shows every receipient the email addresses of other receipients."""
        send_mail(email_subject,
            email_message,
            from_email,
            recipient,
            fail_silently=False)

        messages.success(request, "Your mail was successfully sent")
        return redirect('./thank-you', permanent=False)

    context={
    "form":form,
    "title": title,
    "year": currentYear,
    }
    return render(request, "contact.html", context)

def thanks(request):
    currentYear = datetime.now().year
    return render(request, "thank_you.html", {"year": currentYear,})
