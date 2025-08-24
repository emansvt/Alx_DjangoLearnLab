from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()  

    class Meta:
        model = get_user_model() 
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data) 
        Token.objects.create(user=user) 
        return user
=======
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define password field explicitly and set write_only to true
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'profile_picture', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Don't return password in responses
        }

    def create(self, validated_data):
        # Remove the password from the validated data before passing it to create_user
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)  # Use create_user to hash the password
        user.set_password(password)
        user.save()
        serializers.CharField()

        # Create a token for the user
        Token.objects.create(user=user)
        return user
 
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
