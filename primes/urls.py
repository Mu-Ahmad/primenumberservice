from django.urls import path
from . import views

app_name = "primes"
urlpatterns = [
    path('generate/', views.generate, name="generate"),
    path('monitor/', views.monitor, name = "monitor"),
    path('get/', views.get, name="get"),
]
