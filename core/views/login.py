from django.contrib.auth.views import LoginView


class LoginPage(LoginView):
    template_name = "blog/../templates/core/login.html"

