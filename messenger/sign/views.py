from django.shortcuts import render
from django.views.generic.edit import CreateView
from chat.models import MyUser
from .forms import BaseRegisterForm

class RegisterView(CreateView):
    model = MyUser
    form_class = BaseRegisterForm
    success_url = '/login'
    template_name = 'sign/register.html'
    
