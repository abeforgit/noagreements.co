from django.views.generic import ListView

from core.models import Post


class PostsPage(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "core/posts.html"
    queryset = Post.objects.all().prefetch_related("tags").order_by("pub_date").reverse()
