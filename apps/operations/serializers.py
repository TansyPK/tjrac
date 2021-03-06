from rest_framework import serializers
from operations.models import SelectOperations, NormalOperations, SelectTeacherOperations, SelectCommentOperations


class SelectOperationsSerializers(serializers.ModelSerializer):
    """
    用户选择题操作
    """
    question_id = serializers.IntegerField(label="问题编号", help_text="问题id", required=True, allow_null=False)
    answer_id = serializers.IntegerField(label="回答编号", help_text="回答id", required=True, allow_null=False)
    user_id = serializers.IntegerField(label="用户编号", help_text="用户id", required=True, allow_null=False)
    score = serializers.IntegerField(label="积分", help_text="问题积分", required=True)
    is_correct = serializers.BooleanField(label="正确性", help_text="问答答案是否正确", required=True, allow_null=False)

    class Meta:
        model = SelectOperations
        fields = '__all__'


class NormalOperationsSerializers(serializers.ModelSerializer):
    """
    用户普通问题操作
    """
    question_id = serializers.IntegerField(label="问题编号", help_text="问题id", required=True, allow_null=False)
    answer_id = serializers.IntegerField(label="回答编号", help_text="回答id", required=True, allow_null=False)
    user_id = serializers.IntegerField(label="用户编号", help_text="用户id", required=True, allow_null=False)
    score = serializers.IntegerField(label="积分", help_text="问题积分", required=True)

    class Meta:
        model = NormalOperations
        fields = '__all__'


class SelectTeacherOperationsSerializers(serializers.ModelSerializer):
    """
    学生预约小老师操作
    """
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True, allow_null=False)
    selector_id = serializers.IntegerField(label="学生编号", help_text="学生id", required=True, allow_null=False)
    teacher_id = serializers.IntegerField(label="老师编号", help_text="老师id", required=True, allow_null=False)
    status = serializers.IntegerField(label="邀约状态", help_text="0:失效 1:生效", required=True, allow_null=False)
    room = serializers.IntegerField(label="学习区域", help_text="学习房间号")
    interview_time = serializers.DateTimeField(label="邀约时间", help_text="邀约时间")
    end_time = serializers.DateTimeField(label="结束时间", help_text="结束时间")
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = SelectTeacherOperations
        fields = '__all__'


class SelectCommentOperationsSerializers(serializers.ModelSerializer):
    """
    用户评论操作
    """
    question_id = serializers.IntegerField(label="问题编号", help_text="问题id", required=True, allow_null=False)
    owner = serializers.IntegerField(label="评论所属者", help_text="评论所属者", required=True, allow_null=False)
    content = serializers.CharField(label="评论内容", help_text="评论内容", required=True, allow_null=False)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = SelectCommentOperations
        fields = '__all__'


class SelectOperationsDetailSerializers(serializers.Serializer):
    """
    用户选择题操作详情
    """
    title = serializers.CharField(label="选择题题目", help_text="标题", required=True)
    score = serializers.IntegerField(label="分数", help_text="积分", required=True)
    is_correct = serializers.BooleanField(label="是否正确", help_text="正确与否", required=True)


class NormalOperationsDetailSerializers(serializers.ModelSerializer):
    """
    用户普通问题操作详情
    """
    class Meta:
        model = NormalOperations
        fields = '__all__'


class SelectTeacherOperationsDetailSerializers(serializers.Serializer):
    """
    学生预约小老师详情
    """
    id = serializers.IntegerField(label="预约id", help_text="预约id", required=True)
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)
    selector_id = serializers.IntegerField(label="学生id", help_text="学生id", required=True)
    teacher_id = serializers.IntegerField(label="教师id", help_text="教师id", required=True)
    selector_name = serializers.CharField(label="学生姓名", help_text="学生姓名", required=True, allow_null=False)
    teacher_name = serializers.CharField(label="学生姓名", help_text="学生姓名", required=True, allow_null=False)
    room = serializers.CharField(label="学生姓名", help_text="学生姓名", required=True, allow_null=False)
    status = serializers.CharField(label="学生姓名", help_text="学生姓名", required=True, allow_null=False)


class RoolBackSelectTeacherSerializers(serializers.Serializer):
    """
    撤销预约
    """
    order_id = serializers.IntegerField(label="预约id", help_text="预约id", required=True)
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)


class CompleteSelectTeacherSerializers(serializers.Serializer):
    """
    完成课程
    """
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)


class CancleSelectTeacherSerializers(serializers.Serializer):
    """
    完成课程
    """
    course_id = serializers.IntegerField(label="课程id", help_text="课程id", required=True)
