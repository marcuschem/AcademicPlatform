from django.urls import path
from lectures.views import *

urlpatterns = [
    path('<int:course_id>/<pk>/<int:user_id>/update', UpdateModuleView.as_view(), name='update_module_view'),
    path('lectures/', LecturesView.as_view(), name="lectures"),
    path('lectures/<int:user_id>/<int:course_id>/', LectureView.as_view()),
    path('change/', ChangeCourseView.as_view(), name="manage_course_list"),
    path('change/create/course', CreateCoursesView.as_view(), name='manage_course_create'),
    path('change/<int:user_id>/<int:course_id>/', AdminLectureView.as_view(), name='admin_lecture_view'),
    path('change/<int:user_id>/<int:course_id>/<int:module_id>/', AdminModuleView.as_view(), name='admin_module_view'),
    path('<pk>/delete/', DeleteCourseView.as_view(), name='manage_course_delete'),
    path('<pk>/update/', UpdateCourseView.as_view(), name='manage_course_update'),
    path('<int:course_id>/<pk>/', DeleteModuleView.as_view(), name='manage_module_delete'),
    path('module/<int:module_id>/content/<model_name>/create/', ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/', ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('<int:course_id>/<int:module_id>/content/<pk>/delete/',
         ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('<int:course_id>/module/<int:module_id>/', ModuleContentListView.as_view(), name='module_content_list'),
    path('<int:course_id>/module/create', CreateModuleView.as_view(), name='create_module_view'),
    path('module/order/', ModuleOrderView.as_view(), name='module_order'),
    path('content/order/', ContentOrderView.as_view(), name='content_order'),
    path('', CourseListView.as_view(), name='course_list'),
    path('subject/<slug:subject>/', CourseListView.as_view(), name='course_list_subject'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]
