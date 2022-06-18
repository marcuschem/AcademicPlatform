from django.urls import path
from first_lecture.views import HomeView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]