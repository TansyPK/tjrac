from rest_framework import serializers
from operations.models import SelectOperations, NormalOperations


class SelectOperationsSerializers(serializers.ModelSerializer):
    """
    用户选择题操作
    """
    question_id = serializers.IntegerField(label="问题编号", help_text="问题id", required=True, allow_null=False)
    answer_id = serializers.IntegerField(label="回答编号", help_text="回答id", required=True, allow_null=False)
    user_id = serializers.IntegerField(label="用户编号", help_text="用户id", required=True, allow_null=False)
    score = serializers.IntegerField(label="积分", help_text="问题积分")
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
    score = serializers.IntegerField(label="积分", help_text="问题积分")

    class Meta:
        model = NormalOperations
        fields = '__all__'


class SelectOperationsDetailSerializers(serializers.ModelSerializer):
    """
    用户选择题操作详情
    """
    class Meta:
        model = SelectOperations
        fields = '__all__'


class NormalOperationsDetailSerializers(serializers.ModelSerializer):
    """
    用户普通问题操作详情
    """
    class Meta:
        model = NormalOperations
        fields = '__all__'
