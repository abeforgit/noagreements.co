from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, User, Tag


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Account info', {"fields": (("username", "email"), "password")}),
        ('Personal info',
         {'fields': ('artist_name', ('first_name', 'last_name'), "description")}),
        ("Social info", {"fields": (
            "profile_img", ("bandcamp_url", "spotify_url"), ("facebook_url",
                                                             "instagram_url"))}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    save_on_top = True
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
                    "artist_name",
                    "password1",
                    "password2"
                ]
            }
        )
        ,
    )


def feature(modeladmin, request, queryset):
    featured = Tag.objects.filter(name="featured").first()
    for post in queryset:
        post.tags.add(featured)
        post.save()


feature.short_description = "Add featured tag"


def unfeature(modeladmin, request, queryset):
    featured = Tag.objects.filter(name="featured").first()
    for post in queryset:
        post.tags.remove(featured)
        post.save()


unfeature.short_description = "Remove featured tag"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ["tags"]
    list_display = ["title", "pub_date", "user", "show_tags"]
    list_filter = ["user", "pub_date", "tags"]
    search_fields = ["content"]
    actions = [feature, unfeature]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "show_on_home"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(User, CustomUserAdmin)
