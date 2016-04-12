from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.admin import Group
from django.contrib import admin
from .models import *


# Register your models here.


def mark_selected_as_published(ModelAdmin, request, queryset):
    queryset.update(is_published=True)


def approve_selected_users(ModelAdmin, request, queryset):
    queryset.update(is_active=True)


def block_selected_users(ModelAdmin, request, queryset):
    queryset.update(is_active=False)


class ArticleView(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'publish_date', 'is_published', 'article_view', 'comments_number')
    list_filter = ('publish_date', 'is_published')
    fields = ('title', 'atricle_content', 'image', 'is_published', 'article_tag')
    actions = [mark_selected_as_published]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user_id', None) is None:
            obj.user_id = request.user
        obj.save()


class UserAdmin(admin.ModelAdmin):
    actions = [approve_selected_users, block_selected_users]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'user_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(Comment)
admin.site.register(Article, ArticleView)
admin.site.register(Tag)
admin.site.unregister(Group)
admin.site.register(NewUser, UserAdmin)
admin.site.register(BannedWord)
