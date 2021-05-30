from django import forms
from django.forms import CheckboxSelectMultiple, inlineformset_factory

from core.models import Post, User, ContactLink


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "cover_img", "tags"]
        widgets = {
            "tags": CheckboxSelectMultiple
        }


class CreatorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "description", "profile_img", "artist_name",
                  "username"]


ContactLinkInlineFormset = inlineformset_factory(User, ContactLink,
                                                 fields=["name", "url"], extra=3);
