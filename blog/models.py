from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from blog.signals import number_of_comments


class NewUser(AbstractUser):
    user_image = models.ImageField(upload_to="profile_images", blank=True)


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=200,
        unique=True,
        error_messages={
            'unique': _("This tag already exists."),
        },
    )

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    atricle_content = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(null=True)
    is_published = models.BooleanField(default=False)
    user_id = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    article_view = models.IntegerField(blank=True, null=True)
    article_mark = models.ManyToManyField(NewUser, related_name="user_mark", blank=True)
    article_tag = models.ManyToManyField(Tag)
    comments_number = models.IntegerField(default=0, editable=False)

    def number_of_comments(self):
        comments_counter = self.comment_set.filter().count()
        self.comments_number = comments_counter
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_content = models.TextField()
    is_verified = models.BooleanField(default=False)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(NewUser, related_name="user_comment", on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, blank=True)
    comment_like = models.ManyToManyField(NewUser, blank=True)

    def __str__(self):
        return self.comment_content


class BannedWord(models.Model):
    word = models.CharField(max_length=200)

    def __str__(self):
        return self.word


signals.post_save.connect(number_of_comments, sender=Comment)
signals.post_delete.connect(number_of_comments, sender=Comment)
