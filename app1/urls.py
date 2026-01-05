from django.urls import path
from app1 import views
urlpatterns = [
    path("hello/", views.hello_world),
    path("hello2/", views.hello_world2),
    path("calculator/", views.calculator),
    path("calculator2/",views.calculator2)
]