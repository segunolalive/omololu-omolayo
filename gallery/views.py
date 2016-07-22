from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone

from .forms import ContactForm

from .models import Album, Photo, Post
from urllib.parse import quote_plus


# Create your views here.

#gallery views
def home(request):
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request,"home.html", context)

def album_detail(request, slug):
    album_pictures = get_object_or_404(Album, slug= slug)
    albums = Album.objects.all()
    context = {"albums": albums,
               "pictures": album_pictures,
               }
    return render(request,"album_detail.html", context)



# blog views
def post_list(request):
    query_list = Post.objects.active()
    total_posts = query_list.count
    if request.user.is_staff or request.user.is_superuser:
        query_list = Post.objects.all()

    blog_posts = query_list

    search_query = request.GET.get("q")
    if search_query:
        query_list = query_list.filter(
        Q(title__icontains=search_query) |
        Q(content__icontains=search_query) |
        Q(user__first_name__icontains=search_query) |
        Q(user__last_name__icontains=search_query)
        ).distinct()

    paginator = Paginator(query_list, 5)
    page_request_var = "page"
    page = request.GET.get("page")

    total_posts = paginator.count
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    context = {
    "list": page_list,
    "page_title": "All Articles",
    "page_request_var": page_request_var,
    "all_articles": total_posts,
    "posts": blog_posts,
    }
    return render(request,"blog.html", context)

def post_detail(request, slug):
    posts = Post.objects.active()
    blog_posts = posts
    instance = get_object_or_404(Post, slug= slug)

    share_string = quote_plus(instance.content)

    if instance.draft or instance.published_date > timezone.now():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    context = {
        "title": "instance.title",
        "instance": instance,
        "share_string": share_string,
        "posts": blog_posts,
    }

    return render(request,"post_detail.html", context)


# Contact views
def contact(request):
    title = 'Talk To Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_first_name = form.cleaned_data.get('first_name')
        form_last_name = form.cleaned_data.get('last_name')
        form_message = form.cleaned_data.get('message')

        email_subject = 'New mail from %s' %(form_email)
        email_message = "user email address: %s \n fullname: %s %s \n message:\n %s" %(
            form_email,
            form_first_name,
            form_last_name,
            form_message
            )
        from_email = settings.EMAIL_HOST_USER
        recipient = ['zeusdynamic@yahoo.com'] #a list of  receipient emails

        """This method of sending mails shows every receipient the email addresses of other receipients."""
        send_mail(email_subject,
            email_message,
            from_email,
            recipient,
            fail_silently=False)

        messages.success(request, "Your mail was successfully sent")
        return redirect('./thank-you', permanent=True)

    context={
    "form":form,
    "title": title
    }
    return render(request, "contact.html", context)

def thanks(request):
    return render(request, "thank_you.html", {})
