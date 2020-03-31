from django.views.generic import TemplateView

from blog.models import Post


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_posts"] = Post.objects.order_by("pub_date")[:6]
        context["featured_posts"] = Post.objects.order_by("pub_date").filter(featured=True)
        return context
