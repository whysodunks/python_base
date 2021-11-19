import uuid

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, Group
from django.db import models

# asd = User


class User(AbstractBaseUser, PermissionsMixin):

    class Gender(models.TextChoices):
        NONE = "NONE"
        MALE = "MALE"
        FEMALE = "FEMALE"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, default=None, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True,
                                    help_text='The groups this user belongs to. A user will get all permissions '
                                              'granted to each of their groups.',
                                    related_name='user_set',
                                    related_query_name='user')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True, default=None)
    gender = models.CharField(max_length=255, choices=Gender.choices, default=Gender.NONE)
    address = models.TextField(null=True, blank=True, default=None)
    phone = models.CharField(max_length=255, null=True, blank=True, default=None)
    is_phone_verified = models.BooleanField(default=False)
    avatar = models.TextField(null=True, blank=True, default=None)
    birthday = models.DateField(null=True, blank=True, default=None)
    date_joined = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(default=None, blank=True, null=True, max_length=255)
    modified_at = models.DateTimeField(default=None, blank=True, null=True)
    deleted_by = models.CharField(default=None, blank=True, null=True, max_length=255)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']
    objects = UserManager()

    class Meta:
        db_table = 'auth_user'
