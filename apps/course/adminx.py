import xadmin
from course.models import Course, CourseCategory, CourseFeedBack


class CourseAdmin(object):
    list_display = ['id', 'owner', 'title', 'content', 'room', 'score', 'status', 'type', 'interview_time', 'end_time']
    search_fields = ['id', 'owner', 'title', 'content', 'room', 'score', 'status', 'type', 'interview_time', 'end_time']
    list_filter = ['id', 'owner', 'title', 'content', 'room', 'score', 'status', 'type', 'interview_time', 'end_time']


xadmin.site.register(Course, CourseAdmin)


class CourseCategoryAdmin(object):
    list_display = ['id', 'type', 'type_name']
    search_fields = ['id', 'type', 'type_name']
    list_filter = ['id', 'type', 'type_name']


xadmin.site.register(CourseCategory, CourseCategoryAdmin)


class CourseFeedBackAdmin(object):
    list_display = ['id', 'order_id', 'course_id', 'selector_id', 'teacher_id', 'score', 'content', 'status']
    search_fields = ['id', 'order_id', 'course_id', 'selector_id', 'teacher_id', 'score', 'content', 'status']
    list_filter = ['id', 'order_id', 'course_id', 'selector_id', 'teacher_id', 'score', 'content', 'status']


xadmin.site.register(CourseFeedBack, CourseFeedBackAdmin)
