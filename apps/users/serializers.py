from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情
    """
    class Meta:
        model = User
        fields = '__all__'


class UserDetailCompleteSerializer(serializers.ModelSerializer):
    """
    用户修改详情
    """
    class Meta:
        model = User
        fields = ('name', 'birthday', 'gender', 'mobile', 'email')


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户登录注册
    """
    # 验证用户名是否存在
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    # 输入密码的时候不显示明文
    password = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True
    )

    # 密码加密保存
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdatePasswordSerializer(serializers.Serializer):
    """
    用户更新密码
    """
    # 输入密码的时候不显示明文
    password = serializers.CharField(
        style={'input_type': 'password'}, label="旧密码"
    )
    new_password = serializers.CharField(
        style={'input_type': 'password'}, label="新密码"
    )


class UserToSmallTeacherSerializer(serializers.ModelSerializer):
    """
    用户详情
    """
    class Meta:
        model = User
        fields = ('type', )
