from django.contrib.auth import get_user_model
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.users.serializers import UserRegSerializer, UserDetailSerializer, UserDetailCompleteSerializer, \
    UserUpdatePasswordSerializer, UserToSmallTeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework import generics

from users.models import UserProfile

User = get_user_model()


class UserCreateViewSet(generics.CreateAPIView):
    serializer_class = UserRegSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UserDetailViewSet(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UsersDetailByTypeViewSet(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.filter(type=self.request.GET.get('type')).order_by('-score')


class UserDetailUpdateViewSet(generics.UpdateAPIView):
    serializer_class = UserDetailCompleteSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        user = UserProfile.objects.get(id=instance.id)
        user.score += 10
        if user.type == 0:
            user.type = 2
        user.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        return self.request.user


class UserPasswordUpdateViewSet(generics.UpdateAPIView):
    serializer_class = UserUpdatePasswordSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserUpdatePasswordSerializer(data={
            'password': request.data.get('password'),
            'new_password': request.data.get('new_password')
        })
        serializer.is_valid(raise_exception=True)
        if instance.check_password(serializer.data.get('password')):
            instance.set_password(serializer.data.get('new_password'))
            instance.save()
            return Response({"status": True})
        return Response({"status": False})

    def get_object(self):
        return self.request.user


class UserToSmallTeacherViewSet(generics.UpdateAPIView):
    serializer_class = UserToSmallTeacherSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.score > 500:
            serializer = self.get_serializer(instance, data={'type': 1}, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({"status": True})

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({"status": False})

    def perform_update(self, serializer):
        serializer.save()

    def get_object(self):
        return self.request.user
