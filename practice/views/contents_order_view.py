from practice.models import Contents
from practice.views import OrderView


class ContentsOrderView(OrderView):

    def post(self, request):
        for id, order in self.request_json.items():
            Contents.objects.filter(id=id, question__module__course__author=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})