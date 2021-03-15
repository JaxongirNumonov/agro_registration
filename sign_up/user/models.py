from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=True,
                    is_active=True, **extra_fields):
        'Creates a User with the given username, email and password'
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True,
                                is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_type = models.SmallIntegerField(
        choices=[
            (1, "Yuridik shaxs"),
            (2, "Jismoniy shaxs"),
        ],
        default=1
    )
    full_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-date_joined"]
        get_latest_by = "date_joined"

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)


class TestUser(models.Model):
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=400)
