# Generated by Django 5.1.5 on 2025-02-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp1", "0004_lesson_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("teacher", "Teacher"),
                    ("student", "Student"),
                    ("admin", "Admin"),
                ],
                default="student",
                max_length=7,
            ),
        ),
    ]
