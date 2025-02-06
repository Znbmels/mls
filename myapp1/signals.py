from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Teacher

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'teacher':
        Teacher.objects.create(
            user=instance,
            first_name="Default First Name",  # Укажите значение по умолчанию
            last_name="Default Last Name",   # Укажите значение по умолчанию
            email=instance.email,            # Используйте email из пользователя
            phone="+1234567890"              # Укажите значение по умолчанию
        )