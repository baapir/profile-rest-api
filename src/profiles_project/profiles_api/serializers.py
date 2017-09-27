from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing ou APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializezr for our user profile object"""

    class Meta:
        model = models.UserProfile
        fields=('id', 'email', 'name', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """create and return new user"""

        user = models.UserProfile(
               email = validated_data['email'],
               name = validated_data['name']
        )
        user.set_password(validated_data['password'])

        user.save()

        return user
