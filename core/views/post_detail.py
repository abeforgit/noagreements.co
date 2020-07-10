from django.views.generic import DetailView

from core.models import Post


class PostDetailPage(DetailView):
    template_name = "core/post_detail.html"
    model = Post
