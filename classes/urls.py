from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_classes, name='classes'),
    path('<int:class_id>/', views.class_detail, name='class_detail')
]
