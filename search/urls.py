from django.urls import path


from search.views import *


urlpatterns = [
    path('results/',
         SearchBarGetView.as_view(),
         name='search_bar_get_view'),
]
