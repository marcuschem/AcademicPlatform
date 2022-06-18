from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect


class HomeView(View):
    template_name = 'first_lecture/lecture.html'

    @classmethod
    def get(cls, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, template_name=cls.template_name, *args, **kwargs)
        return HttpResponseRedirect('/login')
