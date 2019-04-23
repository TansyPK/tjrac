from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from operations.models import SelectOperations, NormalOperations
from operations.serializers import SelectOperationsSerializers, NormalOperationsSerializers,\
    SelectOperationsDetailSerializers, NormalOperationsDetailSerializers, SelectTeacherOperationsSerializers
from rest_framework.response import Response
from rest_framework import status


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


class SelectTeacherOperationCreateViewSet(generics.CreateAPIView):
    """
    用户普通问题操作创建
    """
    serializer_class = SelectTeacherOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def create(self, request, *args, **kwargs):
        data = {
            'selector_id': request.user.id,
            'teacher_id': int(request.POST.get('teacher_id')),
            'status': int(request.POST.get('status')),
            'room': int(request.POST.get('room')),
            'interview_time': request.POST.get('interview_time'),
            'end_time': request.POST.get('end_time'),
            'created_time': None,
            'updated_time': None
        }
        serializer_one = SelectTeacherOperationsSerializers(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)
        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


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
