from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Post, User


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


# Register your models here.
admin.site.register(Post)
admin.site.register(User, CustomUserAdmin)
