from django.shortcuts import render

from django.http import HttpResponse
from .models import Article, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
# from django.core.context_processors import csrf
from django.shortcuts import render
from django.template import RequestContext
from .models import *
from blog.forms import UserForm, UserProfileForm
from django.contrib import auth


def index(request):
    all_posts = Article.objects.all()
    data = {'posts': all_posts}
    return render(request, 'blog/index.html', data)


def latest_5(request):
    # posts_5 = Article.objects.all()[:5]
    posts_5 = Article.objects.filter(is_published=True).order_by('-publish_date')[0:5]
    data = {'posts': posts_5}
    return render(request, 'blog/latest_posts.html', data)


def single(request, post_id):
    single = Article.objects.get(pk=post_id)
    data = {'posts': single}
    return render(request, 'blog/single.html', data)


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'user_image' in request.FILES:
                profile.user_image = request.FILES['user_image']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'blog/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'blog/signin.html', c)


def signin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        # return HttpResponse('User is valid, active and authenticated')
        return HttpResponseRedirect('loggedin')
    else:
        return HttpResponseRedirect('invalid')
        # return HttpResponse("Invalid Pass or username")
        print ("fatma")

    # return render(request,'blog/signin.html')


def loggedin(request):
    return render(request, 'blog/loggedin.html')


def invalid(request):
    return render(request, 'blog/invalid.html')


def logout_view(request):
    logout(request)
    return render(request, 'blog/logout_view.html')

# return HttpResponse("You are loggedout")
