from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser

#Типы пользователей на сайте: Админы и пользователи
ADMIN = 1
CLIENT = 2
USER_TYPE = ( #Передаем значения ролям
    (ADMIN, 'ADMIN'), #Первое говорит какая роль, второе как будет высвечиваться
    (CLIENT, 'CLIENT')
)

class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователь' #Кастом в админке
        verbose_name_plural = 'Пользователи' #Кастом во множественном числе
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип ПОльзователя', default=CLIENT) #По дефолту клиент. IntegerFIeld потому что значения ролей по цифрам 1 и 2
    username = models.CharField('username', unique=True, max_length=100) #unique - уникальный, не даст занять юзернейм
    email = models.EmailField('email', null=True, max_length=100) #Первый аргумент - CharField, null=True - оставляет пустым, пишет Null
    first_name = models.CharField('first name', max_length=50, blank=True) #blank - То же что и Null, но пустой, код не ругается
    last_name = models.CharField('last name', max_length=50, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True) #auto_now_add - создает что-то, не меняется после первого раза, auto_now - то же самое, но меняется после изменений
    is_active = models.BooleanField('active', default=True) # defauld=True - по дефолту активен
    is_staff = models.BooleanField(default=False) #Не стафф по дефолту

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

