from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import Form
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from markdown import markdown

from core.forms import PostForm
from core.models import Post, Tag
from core.util.content_sanitizer import sanitize


class CreatePostPage(PermissionRequiredMixin, CreateView):
    permission_required = "core.add_post"
    login_url = "/login"
    model = Post
    form_class = PostForm
    template_name = "core/create_post_page.html"
    success_url = "/post/{id}"
    object: Post

    def form_valid(self, form: Form):
        self.object = form.save(commit=False)
        self.object.content = self.object.content
        self.object.user = self.request.user
        self.object.save()
        self.object.tags.set(form.cleaned_data["tags"])
        return HttpResponseRedirect(self.get_success_url())

