from django.views.generic import TemplateView


class GroupPage(TemplateView):
    template_name = "core/group.html"
