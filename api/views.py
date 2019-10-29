from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from api.serializers import ApplicationSerializer


class ApplicationViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    # queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

