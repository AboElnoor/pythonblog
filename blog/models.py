from __future__ import unicode_literals
from django.db import models


class User(models.Model):
	user_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=200)
	user_image = models.ImageField(upload_to='images/', blank=True)
	role = models.IntegerField()
	is_active = models.BooleanField(default=False)


	def __str__(self):
		return self.user_name

class Article(models.Model):
	title = models.CharField(max_length=200)
	atricle_content = models.TextField()
	image = models.ImageField(upload_to='articleimages/')
	publish_date = models.DateTimeField(null=True)
	is_published = models.BooleanField(default=False)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	article_view = models.IntegerField(blank=True, null=True)
	article_mark = models.ManyToManyField(User, related_name="user_mark", blank=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	comment_content = models.TextField()
	is_verified = models.BooleanField(default=False)
	user_id = models.ForeignKey(User, related_name="user_comment",on_delete=models.CASCADE)
	reply = models.ForeignKey('self', null=True, blank=True)
	comment_like = models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.comment_content

class Tag(models.Model):
	tag_name = models.CharField(max_length=200)
	article_tag = models.ManyToManyField(Article)

class BandWords(models.Model):
	word = models.CharField(max_length=200)
