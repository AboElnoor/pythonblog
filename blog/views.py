from django.shortcuts import render

from django.http import HttpResponse
from .models import Article,Comment 


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

	return render(request,'blog/login.html')



