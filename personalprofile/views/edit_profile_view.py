from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.urls import reverse_lazy

from personalprofile.forms import ProfileEditForm, UserEditForm


class EditProfileView(View):
    template_name = "accounts/edit.html"
    success_url = 'profile_view'

    def get(self, request, profile_id, *args, **kwargs):
        profile_form = ProfileEditForm(instance=request.user)
        user_form = UserEditForm(instance=request.user.profile)
        if request.user.is_authenticated and request.user.profile.id == profile_id:
            return render(request, template_name=self.template_name, context={
                "profile_form": profile_form,
                "user_form": user_form
            }, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("login"))

    def post(self, request, profile_id, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.id == profile_id and request.method == "POST":
            user_form = UserEditForm(
                instance=request.user,
                data=request.POST
            )
            profile_form = ProfileEditForm(
                instance=request.user.profile,
                data=request.POST,
                files=request.FILES
            )
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return HttpResponseRedirect(reverse_lazy(self.success_url, kwargs={
                    "user_id": request.user.id
                }))
            return HttpResponseRedirect(reverse_lazy("login"))
        return HttpResponseRedirect(reverse_lazy("login"))




