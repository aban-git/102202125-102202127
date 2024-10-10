from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer, ProjectSerializer
from django.contrib.auth import authenticate  # 确保已导入 authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserProfileSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        # 尝试获取当前用户所拥有的项目
        try:
            project = request.user.owned_project  # 通过 OneToOne 关系获取项目
            info = {
                "name": project.name,  # 项目名称
                "owner": request.user.username,  # 创建人
                "description": project.description,  # 项目简介
                "requirements": project.requirements,  # 项目要求
            }
            return Response(info, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"error": "该用户尚未创建项目。"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BasicInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = {
            "name": request.user.name,
            "gender": request.user.gender,
            "birthDate": request.user.birth_date,
            "phone": request.user.phone,
            "email": request.user.email,
            "grade": request.user.grade,
            "major": request.user.major,
            "studentId": request.user.student_id,
        }
        return Response(user_profile)

    def put(self, request):
        request.user.name = request.data.get('name', request.user.name)
        request.user.gender = request.data.get('gender', request.user.gender)
        request.user.birth_date = request.data.get('birthDate', request.user.birth_date)
        request.user.phone = request.data.get('phone', request.user.phone)
        request.user.email = request.data.get('email', request.user.email)
        request.user.grade = request.data.get('grade', request.user.grade)
        request.user.major = request.data.get('major', request.user.major)
        request.user.student_id = request.data.get('studentId', request.user.student_id)
        request.user.save()
        return Response({"message": "资料更新成功"}, status=status.HTTP_200_OK)

class SearchUserView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', '')
        return User.objects.filter(username__icontains=username)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'detail': '未找到用户'}, status=status.HTTP_404_NOT_FOUND)
        user = queryset.first()
        serializer = self.get_serializer(user)
        has_project = hasattr(user, 'owned_project')
        data = serializer.data
        data['has_project'] = has_project
        return Response(data, status=status.HTTP_200_OK)

class AddMemberToProjectView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def post(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        project = get_object_or_404(Project, id=project_id)

        if project.owner != request.user:
            return Response({'detail': '你没有权限添加成员到这个项目。'}, status=status.HTTP_403_FORBIDDEN)

        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'detail': '缺少 user_id 参数。'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': '用户不存在。'}, status=status.HTTP_404_NOT_FOUND)

        if hasattr(user, 'owned_project'):
            return Response({'detail': '该用户已经拥有一个项目。'}, status=status.HTTP_400_BAD_REQUEST)

        project.members.add(user)
        return Response({'detail': '成员已添加到项目。'}, status=status.HTTP_200_OK)
