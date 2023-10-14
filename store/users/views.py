from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class LoginView(TemplateView):
    template_name = 'users/login.html'

class RegistrationView(TemplateView):
    template_name = 'users/register.html'

