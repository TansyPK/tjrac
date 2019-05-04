# Create your views here.
from rest_framework import generics
from infomations.serializers import InformationSerializer, InformationCommentSerializer


class InformationsCreateViewSet(generics.CreateAPIView):
    serializer_class = InformationSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class InformationCommentsCreateViewSet(generics.CreateAPIView):
    serializer_class = InformationCommentSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )
