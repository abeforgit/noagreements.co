from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from core.models import Post, ContactLink


class CreatorDetailPage(DetailView):
    context_object_name = "detail_user"
    template_name = "core/creator_detail.html"
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["socials"] = ContactLink.objects.filter(user=self.object)
        context["description_paragraphs"] = self.object.description.split("\n")
        return context
