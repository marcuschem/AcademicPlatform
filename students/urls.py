from django.urls import path
from students.views import (StudentRegistrationView,
                            StudentEnrollCourseView,
                            StudentCourseListView,
                            StudentCourseDetailView)
from django.views.generic import RedirectView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('registration', StudentRegistrationView.as_view(), name='student_registration'),
    path('registration/', RedirectView.as_view(url='/registration')),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<pk>/', cache_page(60 * 15)(StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60 * 15)(StudentCourseDetailView.as_view()), name='student_course_detail_module'),
]
