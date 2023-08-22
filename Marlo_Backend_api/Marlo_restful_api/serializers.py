from rest_framework import serializers
from .models import MarloUser

class MarloUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarloUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MarloUser(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user