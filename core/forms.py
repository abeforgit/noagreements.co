from django import forms
from django_select2 import forms as s2forms

from core.models import Post


class TagsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["name__icontains"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "cover_img", "tags"]
        widgets = {
            "tags": TagsWidget
        }
