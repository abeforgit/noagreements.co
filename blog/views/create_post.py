from django.views.generic import CreateView

from blog.models import Post


class CreatePostPage(CreateView):
    model = Post
    fields = ["title", "content", "user"]
    template_name = "blog/create_post_page.html"
    success_url = "/post/{id}"
