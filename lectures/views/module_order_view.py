from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.views.generic.base import View


from lectures.models import Module


class ModuleOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):

    def post(self, request):
        for id, order in self.request_json.items():
            Module.objects.filter(id=id, course__author=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})