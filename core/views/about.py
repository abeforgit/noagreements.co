from django.views.generic import TemplateView


class AboutPage(TemplateView):
    template_name = "core/about.html"
