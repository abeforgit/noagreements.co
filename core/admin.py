from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, User, Tag, ContactLink, TagPostPosition


class ContactLinkInline(admin.TabularInline):
    model = ContactLink
    extra = 3
    fields = ["name", "url"]


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Account info',
         {"fields": (("username", "email"), "password", "profile_img")}),
        ('Personal info',
         {'fields': (
             'artist_name', ('first_name', 'last_name'), "description")}),
        ('Permissions', {
            'fields': ('groups', 'is_staff', 'is_superuser'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined'), 'classes': ('collapse', )}),
    )
    inlines = [ContactLinkInline]
    save_on_top = True
    list_display = ["username", "artist_name"]

    add_fieldsets = (
        ('Account info',
         {"fields": (("username", "email"), "password", "profile_img")}),
        ('Personal info',
         {'fields': (
             'artist_name', ('first_name', 'last_name'), "description")}),
        ('Permissions', {
            'fields': ('groups', 'is_staff', 'is_superuser'),
        }),
    )

    class Media:
        css = {
            'all': (
                'admin/styles/useradmin.css',
            )
        }


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
    list_display = ["id", "title", "pub_date", "user", "show_tags"]
    list_filter = ["user", "pub_date", "tags"]
    search_fields = ["content"]
    actions = [feature, unfeature]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "show_on_home"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(TagPostPosition)
