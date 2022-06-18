from django.core.cache import cache
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View


from lectures.models import Course, Subject


class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'courses/lecture/list.html'

    def get(self, request, subject=None):

        if request.user.is_authenticated:
            subjects = cache.get('all_subjects')
            if not subjects:
                subjects = Subject.objects.annotate(total_courses=Count('course'))
                cache.set('all_subjects', subjects)
            all_courses = Course.objects.annotate(total_modules=Count('modules'))

            if subject:
                subject = get_object_or_404(Subject, slug=subject)
                key = f'subject_{subject.id}_courses'
                courses = cache.get(key)
                if not courses:
                    courses = all_courses.filter(topic=subject)
                    cache.set(key, courses)
            else:
                courses = cache.get('all_courses')
                if not courses:
                    courses = all_courses
                    cache.set('all_courses', courses)
            return self.render_to_response({'subjects': subjects,
                                            'subject': subject,
                                            'courses': courses})
        return HttpResponseRedirect("/login")
