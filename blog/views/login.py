from django.contrib.auth.views import LoginView


class LoginPage(LoginView):
    template_name = "blog/login.html"

