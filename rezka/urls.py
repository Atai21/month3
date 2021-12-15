from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'films'
urlpatterns = [
    path('films/', views.FilmsView.as_view(), name='film'),
    path('filmparser/', views.ParserFilmsView.as_view(), name='parser')
]
