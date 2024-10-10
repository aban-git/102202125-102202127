from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, BasicInfoView, UserProfileViewSet,SearchUserView,AddMemberToProjectView
from .views import ProjectCreateView
# 创建路由器并注册 UserProfileViewSet
router = DefaultRouter()
router.register(r'users', UserProfileViewSet)

# 合并路由
urlpatterns = [
    path('', include(router.urls)),  # 包含用户相关的 API 路由
    path('register/', RegisterView.as_view(), name='register'),  # 注册路径
    path('login/', LoginView.as_view(), name='login'),          # 登录路径
    path('basicInfo/', BasicInfoView.as_view(), name='basicInfo'),
    path('projectCreate/', ProjectCreateView.as_view(), name='projectCreate'),
    path('searchUser/', SearchUserView.as_view(), name='search-user'),
    path('<int:project_id>/addMember/', AddMemberToProjectView.as_view(), name='add-member'),
]
