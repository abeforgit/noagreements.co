from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class RosterArtPage(TemplateView):
    template_name = "core/roster.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["roster"] = get_user_model().objects.filter(
            groups__name="art")
        context["description"] = "Members at the helm of visual arts"
        context["name"] = "art"
        return context
