from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from qa.models import SelectAnswers, SelectQuestions, NormalAnswers, NormalQuestions
from qa.serializers import SelectQuestionSerializer, NormalQuestionSerializer, SelectAnswerSerializer, NormalAnswerSerializer,\
    SelectAnswerDetailSerializer, SelectQuestionDetailSerializer, NormalAnswerDetailSerializer, NormalQuestionDetailSerializer


class SelectQuestionCreateViewSet(generics.CreateAPIView):
    """
    选择题创建
    """
    serializer_class = SelectQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)


class NormalQuestionCreateViewSet(generics.CreateAPIView):
    """
    普通问题创建
    """
    serializer_class = NormalQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class SelectAnswerCreateViewSet(generics.CreateAPIView):
    """
    选择答案创建
    """
    serializer_class = SelectAnswerSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)


class NormalAnswerCreateViewSet(generics.CreateAPIView):
    """
    普通答案创建
    """
    serializer_class = NormalAnswerSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class SelectQuestionsDetailViewSet(generics.ListAPIView):
    """
    选择问题列表(type获取)
    """
    serializer_class = SelectQuestionDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = SelectQuestions.objects.filter(type=request.GET.get('type'))
        return self.list(request, *args, **kwargs)


class SelectAnswersDetailViewSet(generics.ListAPIView):
    """
    选择回答列表(question_id获取)
    """
    serializer_class = SelectAnswerDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = SelectAnswers.objects.filter(question_id=request.GET.get('question_id'))
        return self.list(request, *args, **kwargs)


class NormalQuestionsDetailViewSet(generics.ListAPIView):
    """
    普通问题列表获取(type获取)
    """
    serializer_class = NormalQuestionDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = NormalQuestions.objects.filter(type=request.GET.get('type'))
        return self.list(request, *args, **kwargs)


class NormalAnswersDetailViewSet(generics.ListAPIView):
    """
    普通回答列表获取(question_id获取)
    """
    serializer_class = NormalAnswerDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = NormalAnswers.objects.filter(question_id=request.GET.get('question_id'))
        return self.list(request, *args, **kwargs)
