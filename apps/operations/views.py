from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from operations.models import SelectOperations, NormalOperations, SelectTeacherOperations, SelectCommentOperations
from operations.serializers import SelectOperationsSerializers,\
    SelectOperationsDetailSerializers, NormalOperationsDetailSerializers,\
    SelectTeacherOperationsSerializers, SelectTeacherOperationsDetailSerializers, SelectCommentOperationsSerializers
from qa.models import SelectQuestions
from rest_framework.response import Response
from rest_framework import status
from users.models import UserProfile


class SelectOperationCreateViewSet(generics.CreateAPIView):
    """
    用户选择题操作创建
    """
    serializer_class = SelectOperationsSerializers
    authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = {
            "question_id": int(request.POST.get('question_id')) if request.POST.get('question_id') else None,
            "answer_id": int(request.POST.get('answer_id')) if request.POST.get('answer_id') else None,
            "user_id": request.user.id,
            "score": int(request.POST.get('score')) if request.POST.get('score') else None,
            'is_correct': bool(int(request.POST.get('is_correct')) if request.POST.get('is_correct') else False)
        }
        user = UserProfile.objects.get(id=request.user.id)
        if data['is_correct']:
            user.score += data['score']
        else:
            user.score += data['score']/2
        user.save()
        serializer_one = SelectOperationsSerializers(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)
        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


class SelectTeacherOperationCreateViewSet(generics.CreateAPIView):
    """
    小老师预约操作创建
    """
    serializer_class = SelectTeacherOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def create(self, request, *args, **kwargs):
        data = {
            'selector_id': request.user.id,
            'teacher_id': int(request.data.get('teacher_id')),
            'status': int(request.data.get('status')),
            'room': int(request.data.get('room')),
            'interview_time': request.data.get('interview_time'),
            'end_time': request.data.get('end_time'),
            'created_time': None,
            'updated_time': None
        }
        serializer_one = SelectTeacherOperationsSerializers(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)
        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


class SelectCommentOperationsCreateViewSet(generics.CreateAPIView):
    """
    用户评论操作创建
    """

    serializer_class = SelectCommentOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def create(self, request, *args, **kwargs):
        data = {
            "question_id": int(request.POST.get('question_id')) if request.POST.get('question_id') else None,
            "owner": request.user.id,
            "content": request.POST.get('content'),
            "created_time": None,
            "updated_time": None
        }
        serializer_one = SelectCommentOperationsSerializers(data=data)
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

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            question = SelectQuestions.objects.get(id=i.question_id)
            serializer = SelectOperationsDetailSerializers(data={
                "title": question.title,
                "score": question.score,
                "is_correct": i.is_correct
            })
            serializer.is_valid(raise_exception=True)
            res.append(serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(queryset)

    def get_queryset(self):
        return SelectOperations.objects.filter(user_id=self.request.user.id)


class NormalOperationDetailViewSet(generics.ListAPIView):
    """
    用户普通问题操作列表获取(user_id获取)
    """
    serializer_class = NormalOperationsDetailSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = NormalOperations.objects.filter(user_id=request.user.id)
        return self.list(request, *args, **kwargs)


class SelectTeacherOperationsDetailViewSet(generics.ListAPIView):
    """
    学生预约小老师列表
    """
    serializer_class = SelectTeacherOperationsDetailSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            teacher = UserProfile.objects.get(id=i.teacher_id)
            student = UserProfile.objects.get(id=i.selector_id)
            serializer = SelectTeacherOperationsDetailSerializers(data={
                'selector_name': student.username,
                'teacher_name':  teacher.username,
                'room': i.room,
                'status': i.status
            })
            serializer.is_valid(raise_exception=True)
            res.append(serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(queryset)

    def get_queryset(self):
        if self.request.user.type == 0:
            return SelectTeacherOperations.objects.filter(selector_id=self.request.user.id)
        else:
            return SelectTeacherOperations.objects.filter(teacher_id=self.request.user.id)


class SelectCommentOperationsDetailViewSet(generics.ListAPIView):
    """
    获取评论列表(question_id 获取)
    """
    serializer_class = SelectCommentOperationsSerializers
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = SelectCommentOperations.objects.filter(question_id=request.GET.get('question_id'))
        return self.list(request, *args, **kwargs)
