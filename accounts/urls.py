from django.conf import settings
from django.contrib.auth.views import (LogoutView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView)
from django.views.generic import RedirectView
from django.urls import path


from accounts.forms import MyLoginForm, CustomPasswordChangeForm
from accounts.views import *

urlpatterns = [
    path('login', CustomLoginView.as_view(authentication_form=MyLoginForm), name='login'),
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('password_reset/', CustomPasswordReview.as_view()),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(form_class=CustomPasswordChangeForm), name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
