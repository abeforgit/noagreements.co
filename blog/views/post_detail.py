from django.views.generic import DetailView

from blog.models import Post


class PostDetailPage(DetailView):
    model = Post
