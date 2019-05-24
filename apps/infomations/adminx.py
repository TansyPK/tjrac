import xadmin
from infomations.models import Information, InformationComment


class InformationAdmin(object):
    list_display = ['id', 'owner', 'question_id', 'content', 'score', 'type']
    search_fields = ['id', 'owner', 'question_id', 'content', 'score', 'type']
    list_filter = ['id', 'owner', 'question_id', 'content', 'score', 'type']


xadmin.site.register(Information, InformationAdmin)


class InformationCommentAdmin(object):
    list_display = ['id', 'owner', 'information_id', 'content']
    search_fields = ['id', 'owner', 'information_id', 'content']
    list_filter = ['id', 'owner', 'information_id', 'content']


xadmin.site.register(InformationComment, InformationCommentAdmin)