from rest_framework import serializers
from qa.models import SelectQuestions, NormalQuestions, SelectAnswers, NormalAnswers


class SelectQuestionSerializer(serializers.ModelSerializer):
    """
    创建选择题
    """
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容", required=True)
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    correct_code = serializers.CharField(label="正确回答", help_text="正确回答的编号", required=True)
    analyzations = serializers.CharField(label="问题解析", help_text="问题解析", required=True)
    score = serializers.IntegerField(label="问题奖励分数", help_text="奖励分数", required=True)
    level = serializers.IntegerField(label="问题等级", help_text="问题权重", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = SelectQuestions
        fields = '__all__'


class SelectAnswerSerializer(serializers.ModelSerializer):
    """
    创建选择题答案
    """
    question_id = serializers.IntegerField(label="回答所属问题", help_text="问题id", required=True)
    content = serializers.CharField(label="内容", help_text="回答内容", required=True)
    select_code = serializers.CharField(label="回答编号", help_text="回答编号", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = SelectAnswers
        fields = '__all__'


class NormalQuestionSerializer(serializers.ModelSerializer):
    """
    创建普通问题
    """
    owner = serializers.IntegerField(label="创建者", help_text="问题创建者", required=True)
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容", required=True)
    score = serializers.IntegerField(label="分数", help_text="问题分数", required=True)
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = NormalQuestions
        fields = '__all__'


class NormalAnswerSerializer(serializers.ModelSerializer):
    """
    创建普通问题答案
    """
    owner = serializers.IntegerField(label="创建者", help_text="回答创建者", required=True)
    question_id = serializers.IntegerField(label="所属问题编号", help_text="问题id", required=True)
    content = serializers.CharField(label="内容", help_text="回答内容", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)

    class Meta:
        model = NormalAnswers
        fields = '__all__'


class SelectQuestionDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="id", help_text="id", required=True)
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容", required=True)
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    correct_code = serializers.CharField(label="正确回答", help_text="正确回答的编号", required=True)
    analyzations = serializers.CharField(label="问题解析", help_text="问题解析", required=True, allow_blank=True)
    score = serializers.IntegerField(label="问题奖励分数", help_text="奖励分数", required=True)
    level = serializers.IntegerField(label="问题等级", help_text="问题权重", required=True)
    answers = serializers.ListField(label="回答列表", help_text="回答列表", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)


class SelectAnswerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SelectAnswers
        fields = '__all__'


class NormalQuestionDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="id", help_text="id", required=True)
    owner = serializers.IntegerField(label="创建者", help_text="问题创建者", required=True)
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容", required=True)
    score = serializers.IntegerField(label="分数", help_text="问题分数", required=True)
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    answers = serializers.ListField(label="回答列表", help_text="回答列表", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)


class NormalQuestionDetailByIdSerializer(serializers.Serializer):
    title = serializers.CharField(label="标题", help_text="选择题标题", required=True)
    score = serializers.IntegerField(label="分数", help_text="问题分数", required=True)
    type = serializers.IntegerField(label="类型", help_text="问题类型", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", allow_null=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", allow_null=True)


class NormalAnswersDetailSerializer(serializers.Serializer):
    owner = serializers.IntegerField(label="创建者", help_text="问题创建者", required=True)
    question_id = serializers.IntegerField(label="问题id", help_text="问题id", required=True)
    content = serializers.CharField(label="内容", help_text="问题内容", required=True)
    created_time = serializers.DateTimeField(label="创建时间", help_text="创建时间", required=True)
    updated_time = serializers.DateTimeField(label="更新时间", help_text="更新时间", required=True)


class NormalAnswerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalAnswers
        fields = '__all__'
