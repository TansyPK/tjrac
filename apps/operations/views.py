from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from operations.models import SelectOperations, NormalOperations
from operations.serializers import SelectOperationsSerializers, NormalOperationsSerializers,\
    SelectOperationsDetailSerializers, NormalOperationsDetailSerializers


class SelectOperationCreateViewSet(generics.CreateAPIView):
    """
    用户选择题操作创建
    """
    serializer_class = SelectOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication,)


class NormalOperationCreateViewSet(generics.CreateAPIView):
    """
    用户普通问题操作创建
    """
    serializer_class = NormalOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )


class SelectOperationDetailViewSet(generics.ListAPIView):
    """
    用户选择题操作列表获取(user_id获取)
    """
    serializer_class = SelectOperationsDetailSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = SelectOperations.objects.filter(user_id=request.user.id)
        return self.list(request, *args, **kwargs)


class NormalOperationDetailViewSet(generics.ListAPIView):
    """
    用户普通问题操作列表获取(user_id获取)
    """
    serializer_class = NormalOperationsDetailSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = NormalOperations.objects.filter(user_id=request.user.id)
        return self.list(request, *args, **kwargs)
