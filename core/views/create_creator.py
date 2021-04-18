import random
import string

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.forms import Form
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from core.forms import CreatorForm
from core.models import User


class CreateCreatorPage(PermissionRequiredMixin, CreateView):
    permission_required = "core.add_user"
    login_url = "/login"
    model = User
    form_class = CreatorForm
    template_name = "core/create_creator_page.html"
    success_url = "/creators/{id}"
    object: User

    def form_valid(self, form: Form):
        self.object = form.save(commit=False)
        self.object.password = ''.join(
            random.choice(string.ascii_letters) for _ in range(10))
        if not self.object.email:
            self.object.email = "dummy@dummy.com"
        self.object.save()
        self.object.groups.add(Group.objects.get(name="creator"))
        return HttpResponseRedirect(self.get_success_url())
