from rest_framework import serializers
from infomations.models import Information, InformationComment


class InformationSerializer(serializers.ModelSerializer):
    """
    创建邀约讲解
    """
    owner = serializers.IntegerField(label="邀约问题所属者", help_text="邀约讲解ID", required=True)
    question_id = serializers.IntegerField(label="问题id", help_text="问题id", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = Information
        fields = '__all__'


class InformationCommentSerializer(serializers.ModelSerializer):
    """
    创建邀约讲解回答
    """
    owner = serializers.IntegerField(label="邀约讲解回答者", help_text="邀约讲解回答者id", required=True)
    information_id = serializers.IntegerField(label="邀约回答id", help_text="邀约回答id", required=True)
    content = serializers.CharField(label="邀约讲解回答内容", help_text="邀约讲解回答内容", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = InformationComment
        fields = '__all__'


class InformationsDetailSerializer(serializers.Serializer):
    question = serializers.DictField(label="问题信息", help_text="问题信息", required=True)
    answers = serializers.ListField(label="回答列表", help_text="回答列表", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)


class InformationsCommentSerializer(serializers.Serializer):
    owner = serializers.IntegerField(label="邀约讲解回答者", help_text="邀约讲解回答者id", required=True)
    information_id = serializers.IntegerField(label="邀约回答id", help_text="邀约回答id", required=True)
    content = serializers.CharField(label="邀约讲解回答内容", help_text="邀约讲解回答内容", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)
