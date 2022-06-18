from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy


class Menu(View):
    template_name = 'menu/menu.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(
                request,
                template_name=self.template_name,
                context={
                    "profile_id": request.user.profile_id
                          },
                *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy("login"))
