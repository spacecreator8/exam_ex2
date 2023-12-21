from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from app.forms import AddOfferForm
from app.models import ProductAndService


def index(request):
    queryset = ProductAndService.objects.all()
    return render(request, 'app/index.html', context={'title': 'Главная', 'queryset': queryset})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'app/login.html'
    extra_context = {
        'template': 'Авторизация'
    }


class CreateOffer(LoginRequiredMixin, CreateView):
    form_class = AddOfferForm
    template_name = 'app/create_offer.html'
    extra_context = {
        'title': 'Создание объявление'
    }
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def my_logout(request):
    logout(request)
    return redirect('/')