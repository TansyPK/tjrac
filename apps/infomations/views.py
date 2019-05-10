# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from qa.models import SelectQuestions, SelectAnswers
from infomations.models import Information, InformationComment
from infomations.serializers import InformationSerializer, InformationCommentSerializer, InformationsDetailSerializer, \
    InformationsCommentSerializer
from qa.serializers import SelectAnswerDetailSerializer, SelectQuestionDetailSerializer
from users.models import UserProfile


class InformationsCreateViewSet(generics.CreateAPIView):
    serializer_class = InformationSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class InformationCommentsCreateViewSet(generics.CreateAPIView):
    serializer_class = InformationCommentSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class InformationsListViewSet(generics.ListAPIView):
    serializer_class = InformationsDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            answers = []
            information_answers= []
            question = SelectQuestions.objects.get(id=i.question_id)
            for j in SelectAnswers.objects.filter(question_id=i.question_id):
                answer_serializer = SelectAnswerDetailSerializer(data={
                    "question_id": j.question_id,
                    "content": j.content,
                    "select_code": j.select_code,
                    "created_time": j.created_time,
                    "updated_time": j.updated_time
                })
                answer_serializer.is_valid(raise_exception=True)
                answers.append(answer_serializer.data)
            question_serializer = SelectQuestionDetailSerializer(data={
                "id": question.id,
                "title": question.title,
                "content": question.content,
                "type": question.type,
                "correct_code": question.correct_code,
                "analyzations": question.analyzations,
                "score": question.score,
                "level": question.level,
                "answers": answers,
                "created_time": question.created_time,
                "updated_time": question.updated_time
            })
            question_serializer.is_valid(raise_exception=True)
            for k in InformationComment.objects.filter(information_id=i.id):
                k_user = UserProfile.objects.get(id=k.owner)
                comment_serializer = InformationsCommentSerializer(data={
                    "owner": k.owner,
                    "username": k_user.username,
                    "information_id": k.information_id,
                    "content": k.content,
                    "created_time": k.created_time,
                    "updated_time": k.updated_time
                })
                comment_serializer.is_valid(raise_exception=True)
                information_answers.append(comment_serializer.data)
            user = UserProfile.objects.get(id=i.owner)
            serializer = InformationsDetailSerializer(data={
                "question": question_serializer.data,
                "answers": information_answers,
                "id": i.id,
                "content": i.content,
                "score": i.score,
                "type": i.type,
                "username": user.username,
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
        return Information.objects.all()
