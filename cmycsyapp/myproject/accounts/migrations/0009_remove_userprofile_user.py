# Generated by Django 5.1.2 on 2024-10-10 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_userprofile_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]
