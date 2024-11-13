import django.contrib.auth.password_validation
import django.core.exceptions
import rest_framework.response
import rest_framework.serializers
import rest_framework.status

import users.models
import reviews.serializers
import documents.serializers
import users.serializers_external

class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        ]

    def validate_password(self, password):
        try:
            django.contrib.auth.password_validation.validate_password(
                password=password
            )
        except django.core.exceptions.ValidationError as e:
            raise rest_framework.serializers.ValidationError(e.messages)
        return password

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = users.models.User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SkillSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.Skill
        fields = [
            'id',
            'user',
            'name',
            'rate'
        ]

class AchievementSerializer(rest_framework.serializers.ModelSerializer):
    users = users.serializers_external.ProfileShortSerializer(many=True, read_only=True)

    class Meta:
        model = users.models.Achievement
        fields = [
            'id',
            'name',
            'description',
            'image',
            'users',
        ]

class AchievementGivingSerializer(rest_framework.serializers.Serializer):
    users = rest_framework.serializers.ListField(
        child=rest_framework.serializers.IntegerField()
    )
    achievements = rest_framework.serializers.ListField(
        child=rest_framework.serializers.IntegerField()
    )

class ProfileSerializer(rest_framework.serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)

    reviews_requests = reviews.serializers.ReviewRequestSerializer(many=True, read_only=True)
    reviews = reviews.serializers.ReviewSerializer(many=True, read_only=True)

    documents = documents.serializers.DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = users.models.User
        fields = [
            'id',

            'username',
            'email',
            'first_name',
            'last_name',
            'profile_image',

            'position',
            'date_of_hiring',

            'skills',
            'achievements',

            'reviews_requests',
            'reviews',

            'documents'
        ]
