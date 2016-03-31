from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	user_name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=200)
	role = models.IntegerField()
	is_active = models.BooleanField(default=False)

class Article(models.Model):
	title = models.CharField(max_length=200)
	atricle_content = models.TextField()
	image = models.CharField(max_length=255)
	publish_date = models.DateTimeField(null=True)
	is_published = models.BooleanField(default=False)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
	article_view = models.IntegerField()
	article_mark = models.ManyToManyField(User, related_name="user_mark")

class Comment(models.Model):
	comment_content = models.TextField()
	is_verified = models.BooleanField(default=False)
	user_id = models.ForeignKey(User, related_name="user_comment",on_delete=models.CASCADE)
	reply = models.ForeignKey('self')
	comment_like = models.ManyToManyField(User)

class Tag(models.Model):
	tag_name = models.CharField(max_length=200)
	article_tag = models.ManyToManyField(Article)