from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy
from . import models, forms
from django.contrib.auth.forms import AuthenticationForm

class RegistrationView(CreateView):
    form_class = forms.RegistrationForm #В forms форма
    template_name = 'users/register.html'

    def get_success_url(self):
        reverse('users:user-list') # Обратились к app_name users, конкретно к path user-list. В url прописано name=user-list

class UserList(ListView):
    template_name = 'users/user_list.html' #users папка в templates
    queryset = models.CustomUser.objects.all()

    def get_queryset(self):
        return models.CustomUser.objects.all()

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_reverse_url(self):
        return reverse_lazy('users:user-list')
