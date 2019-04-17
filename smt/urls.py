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
from apps.users.views import UserCreateViewSet, UserDetailViewSet
from apps.qa.views import NormalQuestionCreateViewSet, SelectQuestionCreateViewSet, NormalAnswerCreateViewSet,\
    SelectAnswerCreateViewSet, SelectQuestionsDetailViewSet, SelectAnswersDetailViewSet, NormalAnswersDetailViewSet,\
    NormalQuestionsDetailViewSet
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('login/', obtain_jwt_token),
    path('signup/', UserCreateViewSet.as_view()),
    path('detail/', UserDetailViewSet.as_view()),
    path('create/normal/question/', NormalQuestionCreateViewSet.as_view()),
    path('create/select/question/', SelectQuestionCreateViewSet.as_view()),
    path('create/normal/answer/', NormalAnswerCreateViewSet.as_view()),
    path('create/select/answer/', SelectAnswerCreateViewSet.as_view()),
    re_path('^list/select/questions/$', SelectQuestionsDetailViewSet.as_view()),
    re_path('^list/select/answers/$', SelectAnswersDetailViewSet.as_view()),
    re_path('^list/normal/questions/$', NormalQuestionsDetailViewSet.as_view()),
    re_path('^list/normal/answers/$', NormalAnswersDetailViewSet.as_view()),
]
