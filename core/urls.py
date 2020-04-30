from django.urls import path

from .views.about import AboutPage
from .views.creator_detail import CreatorDetailPage
from .views.creators import CreatorsPage
from .views.group import GroupPage
from .views.home import HomeView
from blog.views.login import LoginPage
from .views.mixes import MixesPage
from .views.news import NewsPage

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutPage.as_view(), name="about"),
    path("creators", CreatorsPage.as_view(), name="creators"),
    path("creators/<int:pk>", CreatorDetailPage.as_view(), name="creator_detail"),
    path("group", GroupPage.as_view(), name="group"),
    path("news", NewsPage.as_view(), name="news"),
    path("mixes", MixesPage.as_view(), name="mixes"),
]
