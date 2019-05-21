from rest_framework import serializers
from course.models import Course, CourseCategory


class CourseSerializer(serializers.ModelSerializer):
    """
    创建课程
    """
    owner = serializers.IntegerField(label="课程拥有者", help_text="课程所有者id", required=True)
    title = serializers.CharField(label="课程标题", help_text="课程标题", required=True)
    content = serializers.CharField(label="课程内容", help_text="课程简介", required=True)
    room = serializers.IntegerField(label="学习区域", help_text="学习区域id", required=True)
    score = serializers.IntegerField(label="课程分数", help_text="积分", required=True)
    status = serializers.IntegerField(label="课程状态", help_text="课程状态", required=True)
    interview_time = serializers.DateTimeField(label="邀约时间", help_text="邀约时间", required=True)
    end_time = serializers.DateTimeField(label="结束时间", help_text="结束时间", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseCategorySerializer(serializers.ModelSerializer):
    """
    创建课程
    """
    type = serializers.IntegerField(label="课程类别key", help_text="课程类别key", required=True)
    type_name = serializers.CharField(label="课程类别", help_text="课程类别对应中文名", required=True)

    class Meta:
        model = CourseCategory
        fields = '__all__'
