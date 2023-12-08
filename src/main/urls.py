from django.urls import path
from .views import addressee, sender, transport

urlpatterns = [
    path('', sender, name='sender'),
    path('', transport, name='transport'),
    path('', addressee, name='addressee'),
]