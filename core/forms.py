from django import forms
from django.forms import CheckboxSelectMultiple

from core.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "cover_img", "tags"]
        widgets = {
            "tags": CheckboxSelectMultiple
        }
