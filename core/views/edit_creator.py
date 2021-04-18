from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView

from core.forms import CreatorForm
from core.models import User, Post


class EditCreatorPage(PermissionRequiredMixin, UpdateView):
    permission_required = "core.change_user"
    login_url = "/login"
    model = User
    form_class = CreatorForm
    template_name = "core/create_creator_page.html"
    success_url = "/creators/{id}"
    object: Post
