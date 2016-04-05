from django.shortcuts import render

from django.http import HttpResponse
from .models import User,Article,Comment 


def index(request):		
	all_posts = Article.objects.all()
	data = {'posts':all_posts}
	return render(request,'blog/index.html',data)

def latest_5(request):		
	posts_5 = Article.objects.all()[:5]
	data = {'posts':posts_5}
	return render(request,'blog/latest_posts.html',data)


