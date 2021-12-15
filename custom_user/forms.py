from django.contrib.auth import forms
from . import models

class RegistrationForm(forms.UserCreationForm): #Готовые джанговские формы передали в класс
    class Meta:
        model = models.CustomUser
        fields = [ #Создаем поля для заполнения
            'username',
            'first_name',
            'last_name',
            'email'
        ]

