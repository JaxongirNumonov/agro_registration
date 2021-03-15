from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^second/$", views.second, name="second"),
    url(r"^login/$", views.dashboard_login, name="login"),
    url(r"^register/$", views.dashboard_register, name="register"),
    url(r"^logout/$", views.logout, name="logout"),
]