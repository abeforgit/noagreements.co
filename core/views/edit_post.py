from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from markdown import markdown

from core.forms import PostForm
from core.models import Post
from core.util.content_sanitizer import sanitize


class EditPostPage(PermissionRequiredMixin, UpdateView):
    permission_required = "core.add_post"
    login_url = "/login"
    model = Post
    form_class = PostForm
    template_name = "core/create_post_page.html"
    success_url = "/post/{id}"
    object: Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.content = sanitize(markdown(self.object.content))
        self.object.user = self.request.user
        self.object.save()
        self.object.tags.set(form.cleaned_data["tags"])
        return HttpResponseRedirect(self.get_success_url())
