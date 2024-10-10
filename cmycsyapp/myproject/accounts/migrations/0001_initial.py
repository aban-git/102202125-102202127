# Generated by Django 5.1.2 on 2024-10-10 04:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('grade', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('school', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
