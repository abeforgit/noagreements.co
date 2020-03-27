from django.urls import path

from blog.views.create_post import CreatePostPage
from blog.views.post_detail import PostDetailPage

urlpatterns = [
    path("post/new", CreatePostPage.as_view(), name="new_post"),
    path("post/<int:pk>", PostDetailPage.as_view(), name="post_detail")
]
