from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class RosterLabelPage(TemplateView):
    template_name = "core/roster.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["roster"] = get_user_model().objects.filter(
            groups__name="label")
        context["description"] = "Members of the No Agreements music label"
        context["name"] = "label"
        return context
