from django.urls import path
from helloworld.views import hello_world

urlpatterns = [
    path('hello/', hello_world),
]
