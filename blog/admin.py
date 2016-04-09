from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import Group
from django.contrib import admin
from .models import *
# Register your models here.


class ArticleView(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'publish_date', 'is_published', 'article_view', 'comments_number')
    list_filter = ('publish_date', 'is_published')
    fields = ('title', 'atricle_content', 'image', 'is_published', 'article_tag')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user_id', None) is None:
            obj.user_id = request.user
        obj.save()

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
# UserAdmin.fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'age')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
UserAdmin.add_fieldsets = (
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
admin.site.unregister(User)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(BannedWord)


