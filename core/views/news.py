from django.views.generic import TemplateView


class NewsPage(TemplateView):
    template_name = "core/news.html"
