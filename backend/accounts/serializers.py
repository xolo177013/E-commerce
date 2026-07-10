from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'password']

    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            username = validate_data['username'],
            email = validate_data['email'],
            phone_number = validate_data.get('phone_number',''),
            password = validate_data['password']
        )
    
        return user