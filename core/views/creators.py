from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class CreatorsPage(TemplateView):
    template_name = "core/creators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creators"] = get_user_model().objects.filter(groups__name="creator")
        return context
