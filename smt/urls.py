"""smt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path, re_path
from apps.users.views import UserCreateViewSet, UserDetailViewSet, UsersDetailByTypeViewSet
from apps.qa.views import NormalQuestionCreateViewSet, SelectQuestionCreateViewSet, NormalAnswerCreateViewSet,\
    SelectAnswerCreateViewSet, SelectQuestionsDetailViewSet, SelectAnswersDetailViewSet, NormalAnswersDetailViewSet,\
    NormalQuestionsDetailViewSet
from apps.operations.views import SelectOperationCreateViewSet, NormalOperationCreateViewSet, \
    SelectOperationDetailViewSet, NormalOperationDetailViewSet, SelectTeacherOperationCreateViewSet, \
    SelectTeacherOperationsDetailViewSet, SelectCommentOperationsCreateViewSet
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('xadmin/', xadmin.site.urls),  # 资源后台管理
    path('login/', obtain_jwt_token),  # 登陆接口
    path('signup/', UserCreateViewSet.as_view()),  # 注册接口
    path('user/detail/', UserDetailViewSet.as_view()),  # 用户个人信息接口
    re_path('^users/detail/$', UsersDetailByTypeViewSet.as_view()),  # 用户列表接口（学生列表、教师列表）
    path('create/normal/question/', NormalQuestionCreateViewSet.as_view()),  # 创建普通问题接口
    path('create/select/question/', SelectQuestionCreateViewSet.as_view()),  # 创建选择题接口
    path('create/normal/answer/', NormalAnswerCreateViewSet.as_view()),  # 创建普通问题回答接口
    path('create/select/answer/', SelectAnswerCreateViewSet.as_view()),  # 创建选择题回答接口
    path('create/select/comment/', SelectCommentOperationsCreateViewSet.as_view()),  # 创建选择评论接口
    re_path('^list/select/questions/$', SelectQuestionsDetailViewSet.as_view()),  # 选择题列表接口
    re_path('^list/select/answers/$', SelectAnswersDetailViewSet.as_view()),  # 选择题答案列表接口
    re_path('^list/normal/questions/$', NormalQuestionsDetailViewSet.as_view()),  # 普通问题列表接口
    re_path('^list/normal/answers/$', NormalAnswersDetailViewSet.as_view()),  # 普通问题回答列表接口
    re_path('^create/select/operation/$', SelectOperationCreateViewSet.as_view()),  # 用户选择题回答操作接口
    re_path('^create/normal/operation/$', NormalOperationCreateViewSet.as_view()),  # 用户普通问题回答操作接口
    re_path('^list/select/operations/$', SelectOperationDetailViewSet.as_view()),  # 用户选择题操作记录列表接口
    re_path('^list/normal/operations/$', NormalOperationDetailViewSet.as_view()),  # 用户普通问题操作记录列表接口
    re_path('^create/select/teacher/$', SelectTeacherOperationCreateViewSet.as_view()),  # 用户预约小老师接口
    re_path('^list/select/teacher/$', SelectTeacherOperationsDetailViewSet.as_view()),  # 学生/老师预约小老师列表
]
