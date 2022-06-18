from django.urls import path


from practice.views import *


urlpatterns = [
    path('<pk>/', QuestionsView.as_view(), name="question_per_module"),
    path('question/<int:user_id>/<int:question_id>/', QuestionView.as_view(), name="admin_questions"),
    path('question/<int:question_id>/content/<model_name>/create/',
         QuestionCreateUpdateView.as_view(),
         name='question_content_create'),
    path('question/<int:question_id>/content/<model_name>/<id>',
         QuestionCreateUpdateView.as_view(),
         name='question_content_update'),
    path('<int:module_id>/<pk>/update/', QuestionModuleView.as_view(), name='manage_question_update'),
    path('<pk>/create/', CreateQuestionView.as_view(), name='manage_question_create'),
    path('contents/<int:id>/delete/', ContentsQuestionDeleteView.as_view(), name='question_content_delete'),
    path('question/order/', QuestionOrderView.as_view(), name="question_order"),
    path('contents/order/', ContentsOrderView.as_view(), name="contents_order"),
    path('<int:module_id>/<pk>/delete/', DeleteQuestionView.as_view(), name='manage_question_delete'),
    path('question/<int:question_id>/', QuestionContentListView.as_view(), name='module_question_content_list'),
]

