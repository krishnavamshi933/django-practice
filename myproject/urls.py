# myproject/urls.py

from django.urls import path
from myapp.views import hello

urlpatterns = [
    path('hello/', hello, name='hello'),
]
