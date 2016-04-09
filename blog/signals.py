from django.db.models import signals
from django.dispatch import dispatcher


def number_of_comments(sender, instance, signal, *args, **kwargs):
    from blog.models import Article
    for comments in Article.objects.all():
        comments.number_of_comments()
