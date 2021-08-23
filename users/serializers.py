from rest_framework import serializers
from django.contrib.auth.models import User

## Serializes current user
class User_serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', "password"]

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


