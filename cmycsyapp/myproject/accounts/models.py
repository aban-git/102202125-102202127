from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserProfile(AbstractUser):
    # 删除了 user 字段的 default
    name = models.CharField(max_length=100, blank=True, null=True)

    gender = models.CharField(
        max_length=10,
        choices=[('男', '男'), ('女', '女')],
        blank=True,
        null=True
    )
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    grade = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_project',
        null=True,  # 允许为空
        blank=True
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='projects'
    )
    description = models.TextField()
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
