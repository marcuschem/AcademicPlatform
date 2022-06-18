from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.urls import reverse_lazy


from personalprofile.models import Profile


class ProfileView(View):
    template_name = "accounts/profile.html"

    def get(self, request, user_id, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        if request.user.is_authenticated and request.user.id == user_id:
            return render(request,
                          template_name=self.template_name,
                          context={
                              "profile": profile,
                              "profile_id": profile.id
                          }, *args, **kwargs)
        #return HttpResponseRedirect(reverse_lazy("login"))


