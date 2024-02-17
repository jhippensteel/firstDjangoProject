from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('firstDjangoProject/', views.members, name='members'),
    path('firstDjangoProject/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]
