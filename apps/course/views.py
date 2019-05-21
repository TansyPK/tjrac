from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics

from course.models import Course, CourseCategory
from course.serializers import CourseSerializer, CourseCategorySerializer, CourseDetailSerializer

from rest_framework.response import Response
from rest_framework import status

from users.models import UserProfile


class CourseCreateViewSet(generics.CreateAPIView):
    """
    课程创建
    """
    serializer_class = CourseSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)

    def create(self, request, *args, **kwargs):
        data = {
            "owner": request.user.id,
            "title": request.data.get('title'),
            "content": request.data.get('content'),
            "room": int(request.data.get('room')) if request.data.get('room') else 0,
            "score": int(request.data.get('score')) if request.data.get('score') else 0,
            "status": int(request.data.get('status')) if request.data.get('status') else 0,
            "type": int(request.data.get('type')) if request.data.get('type') else 0,
            "interview_time": request.data.get('interview_time'),
            "end_time": request.data.get('end_time'),
            "created_time": None,
            "updated_time": None,
        }
        serializer_one = CourseSerializer(data=data)
        serializer_one.is_valid(raise_exception=True)
        self.perform_create(serializer_one)

        # 给用户添加 10 积分
        user = UserProfile.objects.get(id=request.user.id)
        user.score += 10
        user.save()

        headers = self.get_success_headers(serializer_one.data)
        return Response(serializer_one.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseListViewSet(generics.ListAPIView):
    serializer_class = CourseDetailSerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def list(self, request, *args, **kwargs):
        res = []
        queryset = self.filter_queryset(self.get_queryset())
        for i in queryset:
            course_category = CourseCategory.objects.get(type=i.type)
            course_serializer = CourseDetailSerializer(data={
                "owner": i.owner,
                "title": i.title,
                "content": i.content,
                "room": i.room,
                "score": i.score,
                "status": i.status,
                "type": i.type,
                "type_name": course_category.type_name if course_category else "",
                "interview_time": i.interview_time,
                "end_time": i.end_time,
                "created_time": i.created_time,
                "updated_time": i.updated_time
            })
            course_serializer.is_valid(raise_exception=True)
            res.append(course_serializer.data)
        queryset = res
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(res)

    def get_queryset(self):
        return Course.objects.all()


class CourseCategoryCreateViewSet(generics.CreateAPIView):
    serializer_class = CourseCategorySerializer
    # authentication_classes = (JSONWebTokenAuthentication, )


class CourseCategoryListViewSet(generics.ListAPIView):
    serializer_class = CourseCategorySerializer
    # authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        return CourseCategory.objects.all()
