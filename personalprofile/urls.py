from django.urls import path


from personalprofile.views import *


urlpatterns = [
    path(
        "<int:user_id>/",
        ProfileView.as_view(),
        name="profile_view"
    ),
    path(
        "<int:profile_id>/edit-profile",
        EditProfileView.as_view(),
        name="edit_profile_view"
    ),

]
