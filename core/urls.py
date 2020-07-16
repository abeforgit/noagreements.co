from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView

from .views.about import AboutPage
from .views.creator_detail import CreatorDetailPage
from .views.creators import CreatorsPage
from .views.group import GroupPage
from .views.home import HomeView
from .views.logout import LogoutPage
from .views.mixes import MixesPage
from .views.news import NewsPage
from .views.create_post import CreatePostPage
from .views.post_detail import PostDetailPage
from .views.login import LoginPage

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutPage.as_view(), name="about"),
    path("creators", CreatorsPage.as_view(), name="creators"),
    path("creators/<int:pk>", CreatorDetailPage.as_view(), name="creator_detail"),
    path("group", GroupPage.as_view(), name="group"),
    path("news", NewsPage.as_view(), name="news"),
    path("mixes", MixesPage.as_view(), name="mixes"),
    path("post/add", CreatePostPage.as_view(), name="new_post"),
    path("post/<int:pk>", PostDetailPage.as_view(), name="post_detail"),
    path("login", LoginPage.as_view(), name="login"),
    path("logout", LogoutPage.as_view(), name="logout"),
    path("password_reset", PasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/complete", PasswordResetCompleteView.as_view(), name="password_reset_complete")
]
