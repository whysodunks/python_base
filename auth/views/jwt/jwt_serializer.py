from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # field = "__all__"
        exclude = ('password', 'user_permissions', 'groups')
