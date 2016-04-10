from blog.models import UserProfile
from django.contrib.auth.models import User
from django import forms
import datetime
from .models import Article,Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_image', )


class ArticleForm(forms.Form):
    title= forms.CharField(label='Article Title', max_length=100)
    content = forms.CharField(label='Article Content',widget=forms.Textarea)
    image = forms.ImageField(label='Article Image')
    publish_date= forms.DateTimeField(label='Published Date' ,input_formats=['%Y-%m-%d %H:%M:%S'],initial=datetime.datetime.today)

class ArticleForm2(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('is_published','article_mark','article_view','user_id',)

class CommentForm(forms.Form):
    content = forms.CharField(label=' Comment Content', widget=forms.Textarea)

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']


class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)
