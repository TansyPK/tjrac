from rest_framework import serializers
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    创建课程
    """
    owner = serializers.IntegerField(label="课程拥有者", help_text="课程所有者id", required=True)
    title = serializers.CharField(label="课程标题", help_text="课程标题", required=True)
    content = serializers.CharField(label="课程内容", help_text="课程简介", required=True)
    type = serializers.IntegerField(label="课程类型", help_text="课程类型", required=True)
    score = serializers.IntegerField(label="课程分数", help_text="积分", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = Course
        fields = '__all__'
