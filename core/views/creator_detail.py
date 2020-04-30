from django.contrib.auth.models import User
from django.views.generic import DetailView


class CreatorDetailPage(DetailView):
    template_name = "core/creator_detail.html"
    model = User
