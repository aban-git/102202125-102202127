from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile, Project
from django.contrib.auth import authenticate
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2',
            'name', 'gender', 'birth_date',
            'phone', 'email', 'grade',
            'major', 'student_id', 'school'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "密码不匹配"})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username": "用户名已存在"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = UserProfile.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError({"detail": "无效的凭据"})
        attrs['user'] = user
        return attrs

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'username', 'name', 'gender', 'birth_date',
            'phone', 'email', 'grade', 'major',
            'student_id', 'school'
        )

class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )

    class Meta:
        model = Project
        fields = ['id', 'name', 'owner', 'members', 'description', 'requirements', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        user = self.context['request'].user

        if hasattr(user, 'owned_project'):
            raise serializers.ValidationError("每个用户只能创建一个项目。")

        project = Project.objects.create(owner=user, **validated_data)
        project.members.set(members)
        return project
