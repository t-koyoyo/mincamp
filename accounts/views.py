from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm


# class Top(generic.TemplateView):
#     template_name = 'register/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/sign_in.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'camp/index.html'