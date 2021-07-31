from django.views.generic import TemplateView

from core.models import Post, Tag


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.filter(show_on_home=True)
        context["featured_posts"] = Post.objects.filter(tags__name="featured").order_by("tagpostposition__position")
        return context
