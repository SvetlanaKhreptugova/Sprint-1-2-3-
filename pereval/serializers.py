from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Pass, Image, Coord, User, Level


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'surname', 'last_name', 'email', 'phone']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'data', 'title']


class PassSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pass
        fields = ['id', 'user', 'coords', 'level', 'status', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'images']

    def validate(self, attrs):
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("User data error.")

        if self.instance:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(email=user_data.get('email'))
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.last_name != user_data.get('last_name') or \
                    user.first_name != user_data.get('first_name') or \
                    user.surname != user_data.get('surname') or \
                    user.phone != user_data.get('phone'):
                raise ValidationError("Changes to user fields cannot be edited.")

        super().validate(attrs)

        return attrs
