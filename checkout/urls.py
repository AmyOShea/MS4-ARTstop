from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('signin_guest/', views.signin_guest, name='signin_guest'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook')
]
