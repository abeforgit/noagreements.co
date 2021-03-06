from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView

from .views.about import AboutPage
from .views.create_creator import CreateCreatorPage
from .views.creator_detail import CreatorDetailPage
from .views.creators import CreatorsPage
from .views.edit_creator import EditCreatorPage
from .views.edit_post import EditPostPage
from .views.group import GroupPage
from .views.home import HomeView
from .views.logout import LogoutPage
from .views.mixes import MixesPage
from .views.news import NewsPage
from .views.create_post import CreatePostPage
from .views.post_detail import PostDetailPage
from .views.login import LoginPage
from .views.posts import PostsPage
from .views.splash import SplashView

urlpatterns = [
    path("", SplashView.as_view(), name="splash"),
    path("home", HomeView.as_view(), name="home"),
    path("about", AboutPage.as_view(), name="about"),
    path("creators", CreatorsPage.as_view(), name="creators"),
    path("creators/add", CreateCreatorPage.as_view(), name="new_creator"),
    path("creators/<int:pk>", CreatorDetailPage.as_view(), name="creator_detail"),
    path("creators/<int:pk>/edit", EditCreatorPage.as_view(), name="edit_creator"),
    path("group", GroupPage.as_view(), name="group"),
    path("news", NewsPage.as_view(), name="news"),
    path("mixes", MixesPage.as_view(), name="mixes"),
    path("posts", PostsPage.as_view(), name="posts"),
    path("post/add", CreatePostPage.as_view(), name="new_post"),
    path("post/<int:pk>/edit", EditPostPage.as_view(), name="edit_post"),
    path("post/<int:pk>", PostDetailPage.as_view(), name="post_detail"),
    path("login", LoginPage.as_view(), name="login"),
    path("logout", LogoutPage.as_view(), name="logout"),
    path("password_reset", PasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/complete", PasswordResetCompleteView.as_view(), name="password_reset_complete")
]
