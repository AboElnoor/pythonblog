from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import *
# Register your models here.


class ArticleView(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'is_published', 'article_view')
    list_filter = ('publish_date', 'is_published')
    fields = ('title', 'atricle_content', 'image', 'is_published', 'user_id')

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'age')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
UserAdmin.add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'age')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )

admin.site.register(Comment)
admin.site.register(Article, ArticleView)
admin.site.register(Tag)
admin.site.unregister(User)
admin.site.register(UserProfile, UserAdmin)



