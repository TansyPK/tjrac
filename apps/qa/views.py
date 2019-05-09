from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics

from operations.serializers import NormalOperationsSerializers
from qa.models import SelectAnswers, SelectQuestions, NormalAnswers, NormalQuestions
from users.models import UserProfile
from qa.serializers import SelectQuestionSerializer, NormalQuestionSerializer, SelectAnswerSerializer, \
    NormalAnswerSerializer, \
    SelectAnswerDetailSerializer, SelectQuestionDetailSerializer, NormalAnswerDetailSerializer, \
    NormalQuestionDetailSerializer, NormalQuestionDetailByIdSerializer, NormalAnswersDetailSerializer
from rest_framework.response import Response
from rest_framework import status


class SelectQuestionCreateViewSet(generics.CreateAPIView):
    """
    选择题创建
    """
    serializer_class = SelectQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = {
            "title": request.POST.get('title'),
            "content": request.POST.get('content'),
            "type": int(request.POST.get('type')) if request.POST.get('type') else None,
            "correct_code": request.POST.get('correct_code'),
            "analyzations": request.POST.get('correct_code'),
            "score": int(request.POST.get('score')) if request.POST.get('score') else None,
            "level": int(request.POST.get('level')) if request.POST.get('level') else None,
            "created_time": None,
            "updated_time": None,
        }
        serializer_one = SelectQuestionSerializer(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)
        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


class NormalQuestionCreateViewSet(generics.CreateAPIView):
    """
    普通问题创建
    """
    serializer_class = NormalQuestionSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def create(self, request, *args, **kwargs):
        data = {
            "owner": request.user.id,
            "title": request.data.get('title'),
            "content": request.data.get('content'),
            "score": int(request.data.get('score')) if request.data.get('score') else None,
            "type": int(request.data.get('type')) if request.data.get('type') else None,
            "created_time": None,
            "updated_time": None,
        }
        serializer_one = NormalQuestionSerializer(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)
        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # 用户操作记录
        operation = {
            "question_id": serializer.data['question_id'],
            "answer_id": serializer.data['id'],
            "user_id": serializer.data['owner'],
            "score": 5
        }
        serializer_two = NormalOperationsSerializers(data=operation)
        serializer_two.is_valid(raise_exception=True)
        user = UserProfile.objects.get(id=request.user.id)
        user.score += 5
        user.save()
        serializer_two.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SelectQuestionsDetailViewSet(generics.ListAPIView):
    """
    选择问题列表(type获取)
    """
    serializer_class = SelectQuestionDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            answers = []
            for j in SelectAnswers.objects.filter(question_id=i.id):
                answer_serializer = SelectAnswerDetailSerializer(data={
                    "question_id": j.question_id,
                    "content": j.content,
                    "select_code": j.select_code,
                    "created_time": j.created_time,
                    "updated_time": j.updated_time
                })
                answer_serializer.is_valid(raise_exception=True)
                answers.append(answer_serializer.data)
            serializer = SelectQuestionDetailSerializer(data={
                "title": i.title,
                "content": i.content,
                "type": i.type,
                "correct_code": i.correct_code,
                "analyzations": i.analyzations,
                "score": i.score,
                "level": i.level,
                "answers": answers,
                "created_time": i.created_time,
                "updated_time": i.updated_time
            })
            serializer.is_valid(raise_exception=True)
            res.append(serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(res)

    def get_queryset(self):
        return SelectQuestions.objects.filter(type=self.request.GET.get('type'))


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
    普通问题列表获取(全部获取)
    """
    serializer_class = NormalQuestionDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            answers = []
            for j in NormalAnswers.objects.filter(question_id=i.id):
                answer_serializer = NormalAnswersDetailSerializer(data={
                    "owner": j.owner,
                    "question_id": j.question_id,
                    "content": j.content,
                    "created_time": j.created_time,
                    "updated_time": j.updated_time
                })
                answer_serializer.is_valid(raise_exception=True)
                answers.append(answer_serializer.data)
            serializer = NormalQuestionDetailSerializer(data={
                "owner": i.owner,
                "title": i.title,
                "content": i.content,
                "score": i.score,
                "type": i.type,
                "answers": answers,
                "created_time": i.created_time,
                "updated_time": i.updated_time
            })
            serializer.is_valid(raise_exception=True)
            res.append(serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(res)

    def get_queryset(self):
        return NormalQuestions.objects.all()


class NormalQuestionsDetailByIdViewSet(generics.ListAPIView):
    """
    普通问题列表获取(当前用户)
    """
    serializer_class = NormalQuestionDetailByIdSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res=[]
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            serializer = NormalQuestionDetailByIdSerializer(data={
                "title": i.title,
                "score": i.score,
                "type": i.type,
                "created_time": i.created_time,
                "updated_time": i.updated_time
            })
            serializer.is_valid(raise_exception=True)
            res.append(serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(res)

    def get_queryset(self):
        return NormalQuestions.objects.filter(owner=self.request.user.id)


class NormalAnswersDetailViewSet(generics.ListAPIView):
    """
    普通回答列表获取(question_id获取)
    """
    serializer_class = NormalAnswerDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request, *args, **kwargs):
        self.queryset = NormalAnswers.objects.filter(question_id=request.GET.get('question_id'))
        return self.list(request, *args, **kwargs)
