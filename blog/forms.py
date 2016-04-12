from blog.models import *
from django.contrib.auth.models import User
from django import forms
import datetime
from .models import Article,Comment

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password (again)"), widget=forms.PasswordInput)
    # captcha = CaptchaField()

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2

    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password1','password2', 'user_image',)

# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = NewUser
#         fields = ('user_image', )


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
