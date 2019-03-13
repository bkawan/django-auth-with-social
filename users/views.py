# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView

from users.forms import UserProfileForm
from users.models import User


class UserIndexView(UpdateView):
    template_name = "users/profile.html"
    form_class = UserProfileForm
    queryset = User.objects.all()

    def get_success_url(self):
        return reverse('users:user_profile', kwargs={'pk':self.get_object().id})


class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = "landing_page.html"
