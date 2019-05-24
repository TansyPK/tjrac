import xadmin

from operations.models import SelectOperations, NormalOperations, SelectTeacherOperations, SelectCommentOperations


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


class SelectTeacherOperationsAdmin(object):
    list_display = ['id', 'course_id', 'selector_id', 'teacher_id', 'room', 'status', 'interview_time', 'end_time']
    search_fields = ['id', 'course_id', 'selector_id', 'teacher_id', 'room', 'status', 'interview_time', 'end_time']
    list_filter = ['id', 'course_id', 'selector_id', 'teacher_id', 'room', 'status', 'interview_time', 'end_time']


xadmin.site.register(SelectTeacherOperations, SelectTeacherOperationsAdmin)


class SelectCommentOperationsAdmin(object):
    list_display = ['id', 'question_id', 'owner', 'content']
    search_fields = ['id', 'question_id', 'owner', 'content']
    list_filter = ['id', 'question_id', 'owner', 'content']


xadmin.site.register(SelectCommentOperations, SelectCommentOperationsAdmin)