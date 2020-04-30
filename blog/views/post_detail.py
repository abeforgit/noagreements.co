from django.views.generic import DetailView

from blog.models import Post


class PostDetailPage(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
