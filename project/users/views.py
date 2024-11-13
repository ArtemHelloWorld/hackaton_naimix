import rest_framework.exceptions
import rest_framework.generics
import rest_framework.permissions
import rest_framework.response
import rest_framework.serializers
import rest_framework.status
import rest_framework.views
import rest_framework.viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

import users.models
import users.serializers


class UserCreateAPIView(rest_framework.generics.CreateAPIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    serializer_class = users.serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return rest_framework.response.Response(serializer.data)


class UsersSearchListApiView(rest_framework.generics.ListAPIView):
    serializer_class = users.serializers.ProfileSerializer

    def get_queryset(self):
        return users.models.User.objects.filter(
            username__icontains=self.kwargs['username_filter']
        )

class UsersListApiView(rest_framework.generics.ListAPIView):
    serializer_class = users.serializers.ProfileSerializer

    def get_queryset(self):
        return users.models.User.objects.all()


class ProfileRetrieveUpdateAPIView(
    rest_framework.generics.RetrieveUpdateAPIView
):
    queryset = users.models.User.objects.all()
    lookup_url_kwarg = 'user_id'
    lookup_field = 'id'
    serializer_class = users.serializers.ProfileSerializer

    def perform_update(self, serializer):
        if serializer.instance == self.request.user:
            serializer.save()
        else:
            raise rest_framework.exceptions.PermissionDenied(
                'You can only update your own profile.'
            )

class SkillViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = users.models.Skill.objects.all()
    serializer_class = users.serializers.SkillSerializer
        
class AchievementViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = users.models.Achievement.objects.all()
    serializer_class = users.serializers.AchievementSerializer


class AwardingAchievements(rest_framework.views.APIView):
    def process_request(self, request):
        serialized_data = users.serializers.AchievementGivingSerializer(
            data=request.data
        )
        if serialized_data.is_valid():
            data = serialized_data.validated_data
            achievements = users.models.Achievement.objects.filter(
                id__in=data.get('achievements', [])
            )
            users_objs = users.models.User.objects.filter(
                id__in=data.get('users', [])
            )
            return achievements, users_objs
        else:
            raise rest_framework.exceptions.ValidationError('Wrong data format')
    
    def get_response(self, users_objs):
        users_data = users.serializers.ProfileSerializer(
            users_objs, many=True
        ).data
        return rest_framework.response.Response(users_data)
        
    @swagger_auto_schema(
        request_body=users.serializers.AchievementGivingSerializer,
    )
    def post(self, request):
        achievements, users_objs = self.process_request(request)
        for user in users_objs:
            user.achievements.add(*achievements)
        return self.get_response(users_objs)
    
    @swagger_auto_schema(
        request_body=users.serializers.AchievementGivingSerializer,
    )
    def delete(self, request):
        achievements, users_objs = self.process_request(request)
        for user in users_objs:
            user.achievements.remove(*achievements)
        return self.get_response(users_objs)
