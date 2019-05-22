from rest_framework import serializers
from course.models import Course, CourseCategory, CourseFeedBack


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
    type = serializers.IntegerField(label="课程类别", help_text="课程类别", required=True)
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


class CourseDetailSerializer(serializers.Serializer):
    """
    课程详细列表
    """
    id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)
    owner = serializers.IntegerField(label="课程拥有者", help_text="课程所有者id", required=True)
    title = serializers.CharField(label="课程标题", help_text="课程标题", required=True)
    content = serializers.CharField(label="课程内容", help_text="课程简介", required=True)
    room = serializers.IntegerField(label="学习区域", help_text="学习区域id", required=True)
    score = serializers.IntegerField(label="课程分数", help_text="积分", required=True)
    status = serializers.IntegerField(label="课程状态", help_text="课程状态", required=True)
    type = serializers.IntegerField(label="课程类别", help_text="课程类别", required=True)
    type_name = serializers.CharField(label="课程类别名称", help_text="课程类别名称", required=True)
    interview_time = serializers.DateTimeField(label="邀约时间", help_text="邀约时间", required=True)
    end_time = serializers.DateTimeField(label="结束时间", help_text="结束时间", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)


class CourseFeedBackSerializer(serializers.ModelSerializer):
    """
    课程反馈
    """
    order_id = serializers.IntegerField(label="预约id", help_text="预约id", required=True)
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)
    selector_id = serializers.IntegerField(label="评论人id", help_text="评论人id", required=True)
    teacher_id = serializers.IntegerField(label="老师id", help_text="老师id", required=True)
    score = serializers.IntegerField(label="评分", help_text="评分", required=True)
    content = serializers.CharField(label="内容", help_text="内容", required=True)
    status = serializers.IntegerField(label="状态", help_text="状态", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = CourseFeedBack
        fields = '__all__'


class CourseFeedBackDetailSerializer(serializers.Serializer):
    """
    课程评价详情
    """
    username = serializers.CharField(label="反馈者", help_text="反馈者姓名", required=True)
    content = serializers.CharField(label="内容", help_text="内容", required=True)
    score = serializers.IntegerField(label="分数", help_text="分数", required=True)
    course_name = serializers.CharField(label="课程名称", help_text="课程名称", required=True)
    status = serializers.IntegerField(label="状态", help_text="状态", required=True)
