from django.urls import path
from .views import hello_world_view, date_view, random_view, blog_view, post_detail

urlpatterns = [
    path("hello", hello_world_view),
    path("date", date_view),
    path('random', random_view),
    path('', blog_view),
    path('<int:pk>/', post_detail),
]