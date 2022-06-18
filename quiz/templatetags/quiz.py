from django import template


from practice.models import QuestionText, QuestionFile, QuestionImage, Choice, Answer


register = template.Library()


@register.filter
def possible_options(obj):
    try:
        return {
            'options': [content.question_item for content in obj if isinstance(content.question_item,
                                                                               Choice)],
            'answers': [content.question_item for content in obj if isinstance(content.question_item,
                                                                               Answer)]
        }
    except AttributeError:
        return None


@register.filter
def question_body(obj):
    try:
        return [content.question_item for content in obj if isinstance(content.question_item,
                                                                       (QuestionText,
                                                                        QuestionImage,
                                                                        QuestionFile))]

    except AttributeError:
        return None
