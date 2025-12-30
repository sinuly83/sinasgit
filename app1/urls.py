from django.urls import path
from app1 import views
urlpatterns = [
    path("hello/", views.hello_world),
    path("hello2/", views.hello_world2),
]