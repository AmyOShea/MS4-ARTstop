from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('signin_guest', views.signin_guest, name='signin_guest'),
]
