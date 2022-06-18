from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.views.generic.base import View


class OrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    pass
