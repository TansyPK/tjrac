from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from qa.serializers import SelectQuestionSerializer, NormalQuestionSerializer, SelectAnswerSerializer, NormalAnswerSerializer


class SelectQuestionCreateViewSet(generics.CreateAPIView):
    serializer_class = SelectQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)


class NormalQuestionCreateViewSet(generics.CreateAPIView):
    serializer_class = NormalQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class SelectAnswerCreateViewSet(generics.CreateAPIView):
    serializer_class = SelectAnswerSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)


class NormalAnswerCreateViewSet(generics.CreateAPIView):
    serializer_class = NormalAnswerSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )
