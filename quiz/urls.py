from django.urls import path


from quiz.views import *


urlpatterns = [
    path('quices/course/<pk>/', FinalQuizView.as_view(), name='final_quiz_view'),
    path('quices/', CourseQuizListView.as_view(), name='course_quiz_list_view'),
    path('quices/partial/done/score', ScoreQuizView.as_view(), name='score_quiz_view'),
    path('quices/total/done/score', ScoreFinalQuizView.as_view(), name='score_final_quiz_view'),
    path('quices/modules/<pk>/', ModularQuizListView.as_view(), name='modular_quiz_list_view'),
    path('quices/module/<pk>/', ModularQuizView.as_view(), name='modular_quiz_view'),
]
