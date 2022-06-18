from django.urls import path
from menu.views import Menu


urlpatterns = [
    path('', Menu.as_view(), name='menu'),
]
