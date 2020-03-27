import bleach
from django.forms import Form
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from markdown import markdown

from blog.models import Post
from blog.util.content_sanitizer import sanitize


class CreatePostPage(CreateView):
    object: Post
    model = Post
    fields = ["title", "content", "user"]
    template_name = "blog/create_post_page.html"
    success_url = "/post/{id}"

    def form_valid(self, form: Form):
        self.object = form.save(commit=False)
        self.object.content = sanitize(markdown(self.object.content))
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
