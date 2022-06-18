from practice.models import Question
from practice.views import OrderView


class QuestionOrderView(OrderView):

    def post(self, request):
        for id, order in self.request_json.items():
            Question.objects.filter(id=id, module__course__author=request.user).update(order=order)
        return self.render_json_response({'saved': 'OK'})