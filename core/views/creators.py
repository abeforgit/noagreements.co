from django.contrib.auth.models import User
from django.views.generic import TemplateView


class CreatorsPage(TemplateView):
    template_name = "core/creators.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["creators"] = User.objects.filter(groups__name="creator")
        return context
