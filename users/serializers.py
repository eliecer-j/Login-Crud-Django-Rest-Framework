from rest_framework import serializers
from users.models import User
class User_serializers(serializers.ModelSerializer):

    email = serializers.CharField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    password_temp = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_temp']


    def validate(self, data):
        if data['password_temp'] != data['password']:
            raise serializers.ValidationError(detail='las contraseñas no considen')
        return data

    def create(self, validated_data):

        validated_data.pop('password_temp')

        User.objects.create(**validated_data)
        return User