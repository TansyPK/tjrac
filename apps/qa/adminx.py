import xadmin

from qa.models import SelectAnswers, SelectQuestions, NormalAnswers, NormalQuestions, ContentQuestion, ContentAnswers


class SelectAnswersAdmin(object):
    list_display = ['id', 'question_id', 'content', 'select_code']
    search_fields = ['id', 'question_id', 'content', 'select_code']
    list_filter = ['id', 'question_id', 'content', 'select_code']


xadmin.site.register(SelectAnswers, SelectAnswersAdmin)


class SelectQuestionsAdmin(object):
    list_display = ['id', 'title', 'content', 'type', 'correct_code']
    search_fields = ['id', 'title', 'content', 'type', 'correct_code']
    list_filter = ['id', 'title', 'content', 'type', 'correct_code']


xadmin.site.register(SelectQuestions, SelectQuestionsAdmin)


class NormalAnswersAdmin(object):
    list_display = ['id', 'owner', 'question_id', 'content']
    search_fields = ['id', 'owner', 'question_id', 'content']
    list_filter = ['id', 'owner', 'question_id', 'content']


xadmin.site.register(NormalAnswers, NormalAnswersAdmin)


class NormalQuestionsAdmin(object):
    list_display = ['id', 'owner', 'content', 'type', 'title']
    search_fields = ['id', 'owner', 'content', 'type', 'title']
    list_filter = ['id', 'owner', 'content', 'type', 'title']


xadmin.site.register(NormalQuestions, NormalQuestionsAdmin)


class ContentQuestionAdmin(object):
    list_display = ['id', 'content', 'type', 'title']
    search_fields = ['id', 'content', 'type', 'title']
    list_filter = ['id', 'content', 'type', 'title']


xadmin.site.register(ContentQuestion, ContentQuestionAdmin)


class ContentAnswersAdmin(object):
    list_display = ['id', 'owner', 'question_id', 'content']
    search_fields = ['id', 'owner', 'question_id', 'content']
    list_filter = ['id', 'owner', 'question_id', 'content']


xadmin.site.register(ContentAnswers, ContentAnswersAdmin)
