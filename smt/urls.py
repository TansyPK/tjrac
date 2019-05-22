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
from apps.users.views import UserCreateViewSet, UserDetailViewSet, UsersDetailByTypeViewSet, UserDetailUpdateViewSet, \
    UserPasswordUpdateViewSet, UserToSmallTeacherViewSet
from apps.qa.views import NormalQuestionCreateViewSet, SelectQuestionCreateViewSet, NormalAnswerCreateViewSet, \
    SelectAnswerCreateViewSet, SelectQuestionsDetailViewSet, SelectAnswersDetailViewSet, NormalAnswersDetailViewSet, \
    NormalQuestionsDetailViewSet, NormalQuestionsDetailByIdViewSet
from apps.operations.views import SelectOperationCreateViewSet, \
    SelectOperationDetailViewSet, NormalOperationDetailViewSet, SelectTeacherOperationCreateViewSet, \
    SelectTeacherOperationsDetailViewSet, SelectCommentOperationsCreateViewSet, SelectCommentOperationsDetailViewSet, \
    RoolBackSelectTeacherViewSet, SelectStudentOperationsDetailViewSet, CancleSelectTeacherViewSet, \
    CompleteSelectTeacherViewSet
from apps.course.views import CourseCreateViewSet, CourseListViewSet, CourseCategoryCreateViewSet, \
    CourseCategoryListViewSet, MyCourseListViewSet, CourseFeedBackCreateViewSet, CourseFeedBackListViewSet
from rest_framework_jwt.views import obtain_jwt_token

from infomations.views import InformationsCreateViewSet, InformationCommentsCreateViewSet, InformationsListViewSet

urlpatterns = [
    # 后台
    path('xadmin/', xadmin.site.urls),  # 资源后台管理

    # 登陆注册
    path('login/', obtain_jwt_token),  # 登陆接口
    path('signup/', UserCreateViewSet.as_view()),  # 注册接口

    # 用户个人页
    path('user/detail/', UserDetailViewSet.as_view()),  # 用户个人信息接口
    path('update/user/detail/', UserDetailUpdateViewSet.as_view()),  # 用户个人信息更新接口
    path('update/user/password/', UserPasswordUpdateViewSet.as_view()),  # 用户修改密码接口
    path('update/user/smt/', UserToSmallTeacherViewSet.as_view()),  # 用户申请小老师接口
    re_path('^list/me/questions/$', NormalQuestionsDetailByIdViewSet.as_view()),  # 我的讨论区发布

    # 闯关答题
    path('create/select/question/', SelectQuestionCreateViewSet.as_view()),  # 创建闯关问题接口（系统）
    path('create/select/answer/', SelectAnswerCreateViewSet.as_view()),  # 创建闯关回答接口（系统）
    path('create/select/comment/', SelectCommentOperationsCreateViewSet.as_view()),  # 创建选择评论接口
    re_path('^list/select/comment/$', SelectCommentOperationsDetailViewSet.as_view()),  # 选择题评论列表
    re_path('^list/select/questions/$', SelectQuestionsDetailViewSet.as_view()),  # 闯关选择题
    # re_path('^list/select/answers/$', SelectAnswersDetailViewSet.as_view()),  # 闯关选择题回答（已集成至获取问题接口）
    re_path('^create/select/operation/$', SelectOperationCreateViewSet.as_view()),  # 闯关记录接口
    re_path('^list/select/operations/$', SelectOperationDetailViewSet.as_view()),  # 闯关记录列表接口

    # 邀约讲解
    path('create/information/', InformationsCreateViewSet.as_view()),  # 创建邀约讲解
    path('create/information/comment/', InformationCommentsCreateViewSet.as_view()),  # 创建邀约讲解回答
    re_path('^list/informations/$', InformationsListViewSet.as_view()),  # 讲解邀约列表

    # 讨论区
    path('create/normal/question/', NormalQuestionCreateViewSet.as_view()),  # 创建讨论区问题接口
    path('create/normal/answer/', NormalAnswerCreateViewSet.as_view()),  # 创建讨论区问题回答
    re_path('^list/normal/questions/$', NormalQuestionsDetailViewSet.as_view()),  # 讨论区列表
    re_path('^list/normal/answers/$', NormalAnswersDetailViewSet.as_view()),  # 讨论区回答详情接口
    re_path('^list/normal/operations/$', NormalOperationDetailViewSet.as_view()),  # 讨论区记录列表接口

    # 小老师
    path('create/course/', CourseCreateViewSet.as_view()),  # 创建小老师课程接口
    path('create/course/category/', CourseCategoryCreateViewSet.as_view()),  # 创建小老师课程类别接口
    path('list/course/category/', CourseCategoryListViewSet.as_view()),  # 小老师课程类别列表接口
    path('cancle/course/order/', RoolBackSelectTeacherViewSet.as_view()),  # 预约撤销接口
    path('cancle/course/', CancleSelectTeacherViewSet.as_view()),  # 删除课程接口
    path('complete/course/', CompleteSelectTeacherViewSet.as_view()),  # 完成课程接口
    path('create/course/feedback/', CourseFeedBackCreateViewSet.as_view()),  # 创建课程评价
    re_path('^create/select/teacher/$', SelectTeacherOperationCreateViewSet.as_view()),  # 预约接口
    re_path('^list/select/teacher/$', SelectTeacherOperationsDetailViewSet.as_view()),  # 我的预约
    re_path('^list/select/student/$', SelectStudentOperationsDetailViewSet.as_view()),  # 我的课程
    re_path('^list/course/mine/$', MyCourseListViewSet.as_view()),  # 我发布的课程
    re_path('^list/courses/$', CourseListViewSet.as_view()),  # 小老师课程列表
    re_path('^list/course/feedback/$', CourseFeedBackListViewSet.as_view()),  # 我的评价

    # 荣誉榜
    re_path('^users/detail/$', UsersDetailByTypeViewSet.as_view()),  # 荣誉榜 type 0 学生 type 1 小老师
]
