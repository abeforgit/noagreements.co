from django.urls import path

from .views.home import HomeView
from blog.views.login import LoginPage

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginPage.as_view(), name="login")
]
