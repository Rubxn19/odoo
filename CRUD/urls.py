from unicodedata import name
from django.urls import path
from django.urls import path, include

from . import views

#app_name = 'crudapi'

urlpatterns = [
    path("Home", views.index, name="index"),
    path("", views.registration, name="registration"),
    path("", views.login, name="login"),
    # path("create",views.create, name="create")
]