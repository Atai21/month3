from django.urls import path
from .views import hello_world_view, date_view, random_view


urlpatterns = [
    path("hello", hello_world_view),
    path("date", date_view),
    path('random', random_view)
]