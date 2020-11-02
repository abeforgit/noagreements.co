from django import forms
from django_select2 import forms as s2forms

from core.models import Post, Tag


class TagsWidget(s2forms.ModelSelect2MultipleWidget):
    queryset = Tag.objects.all()
    model = Tag
    search_fields = ["name__icontains"]

    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs=extra_attrs)
        attrs["data-minimum-input-length"] = 0;
        return attrs




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "cover_img", "tags"]
        widgets = {
            "tags": TagsWidget
        }
