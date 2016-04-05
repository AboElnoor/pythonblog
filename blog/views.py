from django.shortcuts import render

from django.http import HttpResponse
from .models import Article,Comment
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout


def index(request):		
	all_posts = Article.objects.all()
	data = {'posts':all_posts}
	return render(request,'blog/index.html',data)

def latest_5(request):		
	# posts_5 = Article.objects.all()[:5]
	posts_5 =Article.objects.filter(is_published=True).order_by('-publish_date')[0:5]
	data = {'posts':posts_5}
	return render(request,'blog/latest_posts.html',data)

def single(request,post_id):
	single = Article.objects.get(pk=post_id)
	data = {'posts':single}
	return render(request,'blog/single.html',data)
def register(request):		

	return render(request,'blog/register.html')

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'blog/signin.html', c)
	
def signin(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
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
	return render(request,'blog/logout_view.html')
	# return HttpResponse("You are loggedout")
