from django.views.generic import TemplateView

from core.models import Post, Tag


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        context["tags"] = {
            tag.name: {"tag": tag, "post_positions": tag.tagpostposition_set.order_by(
                "position")}
            for tag in tags}

        context["featured_posts"] = Post.objects.filter(
            tags__name="featured").order_by("tagpostposition__position")
        return context
