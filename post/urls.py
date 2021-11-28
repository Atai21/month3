from django.urls import path
from .views import hello_world_view, date_view, random_view, blog_view, post_detail, create_comment, test

urlpatterns = [
    path("hello", hello_world_view),
    path("date", date_view),
    path('random', random_view),
    path('', blog_view, name="blog"),
    path('<int:pk>/', post_detail, name='post-detail'),
    path("<int:pk>/comment/", create_comment),
    path("test", test)
]