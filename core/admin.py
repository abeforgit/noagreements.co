from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, User, Tag


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Extra info",
            {
                "fields": [
                    "profile_img"
                ]
            }
        )
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "email",
                    "username",
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
