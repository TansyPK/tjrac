from rest_framework import serializers
from qa.models import SelectQuestions, NormalQuestions


class SelectQuestionSerializer(serializers.ModelSerializer):
    """
    创建选择题
    """
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容")
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    correct_code = serializers.CharField(label="正确回答", help_text="正确回答的编号")
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = SelectQuestions
        fields = '__all__'


class NormalQuestionSerializer(serializers.ModelSerializer):
    """
    创建选择题
    """
    owner = serializers.IntegerField(label="创建者", help_text="问题创建者", required=True)
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容")
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = NormalQuestions
        fields = '__all__'
