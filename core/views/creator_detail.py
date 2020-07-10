from django.contrib.auth.models import User
from django.views.generic import DetailView

from core.models import Post


class CreatorDetailPage(DetailView):
    template_name = "core/creator_detail.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(user_id=self.object.id)
        return context
