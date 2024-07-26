from .models import User
from rest_framework import serializers
from django.core.validators import EmailValidator

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    class Meta:
        model = User
        fields = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'profile_picture',
        'bio',
        'phone_number',
        'date_of_birth',
        'address',
        'city',
        'province',
        'postal_code',
        'last_purchase_date',
        ]
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user