from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View


from lectures.models import Course, Module, Video, Image, File
from search.models import SearchingAction


class SearchBarGetView(View):
    template_name = "search/search.html"

    @staticmethod
    def searching_courses(key):
        author_first_name = Q(author__first_name__icontains=key)
        author_last_name = Q(author__last_name__icontains=key)
        author_username = Q(author__username__icontains=key)
        author_id = Q(author__id__icontains=key)

        by_author = author_first_name | author_last_name | author_username | author_id

        by_topic_title = Q(topic__title__icontains=key)
        by_topic_slug = Q(topic__slug__icontains=key)

        by_topic = by_topic_title | by_topic_slug

        by_slug = Q(slug__icontains=key)

        by_overview = Q(overview__icontains=key)

        by_id = Q(id__icontains=key)

        return Course.objects.filter(by_author|by_topic|by_slug|by_overview|by_id)

    @staticmethod
    def searching_modules(key):
        author_first_name = Q(course__author__first_name__icontains=key)
        author_last_name = Q(course__author__last_name__icontains=key)
        author_user_name = Q(course__author__username__icontains=key)
        author_id = Q(course__author__id__icontains=key)

        by_author = author_first_name | author_last_name | author_user_name | author_id

        course_topic_title = Q(course__topic__title__icontains=key)
        course_topic_slug = Q(course__topic__slug__icontains=key)

        by_topic = course_topic_title | course_topic_slug

        by_course_slug = Q(course__slug__icontains=key)

        by_course_overview = Q(course__overview__icontains=key)

        by_description = Q(description__icontains=key)

        by_course_id = Q(course__id__icontains=key)

        by_id = Q(id__icontains=key)

        query = by_author | by_topic | by_course_slug | by_course_overview | by_description | by_course_id | by_id

        return Module.objects.filter(query)

    @staticmethod
    def searching_videos(key):
        by_author = Q(author__username__icontains=key)

        by_video = Q(video__icontains=key)

        by_title = Q(title__icontains=key)

        return Video.objects.filter(by_author | by_video | by_title)

    @staticmethod
    def searching_image(key):
        by_author = Q(author__username__icontains=key)

        by_image = Q(image__icontains=key)

        by_title = Q(title__icontains=key)

        return Image.objects.filter(by_author | by_image | by_title)

    @staticmethod
    def searching_file(key):
        by_author = Q(author__username__icontains=key)

        by_file = Q(file__icontains=key)

        by_title = Q(title__icontains=key)

        return File.objects.filter(by_author | by_file | by_title)

    def searching(self, key):
        courses = self.searching_courses(key)

        modules = self.searching_modules(key)

        files = self.searching_file(key)

        images = self.searching_image(key)

        videos = self.searching_videos(key)

        return courses, modules, files, images, videos

    def get(self, request, *args, **kwargs):
        key = request.GET.get("search", " ")
        action = SearchingAction.objects.create(body=key, author=request.user)
        action.save()
        courses, modules, files, images, videos = self.searching(key)
        context = {
            'user_id': request.user.id,
            'courses': courses,
            'modules': modules,
            'files': files,
            'images': images,
            'videos': videos,
            'key': key
        }
        if any([
            courses,
            modules,
            files,
            images,
            videos
        ]):
            action.was_successful = True
        action.save()

        return render(request,
                      template_name=self.template_name,
                      context=context,
                      *args, **kwargs)











