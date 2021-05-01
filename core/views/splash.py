from django.views.generic import TemplateView


class SplashView(TemplateView):
    template_name = "core/splash_page.html"
