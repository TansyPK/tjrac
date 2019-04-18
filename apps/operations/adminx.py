import xadmin

from operations.models import SelectOperations, NormalOperations


class SelectOperationsAdmin(object):
    list_display = ['id', 'question_id', 'answer_id', 'user_id', 'score', 'is_correct']
    search_fields = ['id', 'question_id', 'answer_id', 'user_id', 'score', 'is_correct']
    list_filter = ['id', 'question_id', 'answer_id', 'user_id', 'score', 'is_correct']


xadmin.site.register(SelectOperations, SelectOperationsAdmin)


class NormalOperationsAdmin(object):
    list_display = ['id', 'question_id', 'answer_id', 'user_id', 'score']
    search_fields = ['id', 'question_id', 'answer_id', 'user_id', 'score']
    list_filter = ['id', 'question_id', 'answer_id', 'user_id', 'score']


xadmin.site.register(NormalOperations, NormalOperationsAdmin)
