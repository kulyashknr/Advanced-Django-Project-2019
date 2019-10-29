from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from api.models import Vacancy
from api.serializers import VacancySerializer


class VacancyViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

