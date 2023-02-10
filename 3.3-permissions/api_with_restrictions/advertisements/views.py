from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly, FavoritePermission


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy", "get_favorites", "mark_as_favorite"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly(), FavoritePermission()]
        return []

    def get_queryset(self):
        if self.action == 'get_favorites':
            if self.request.user.is_anonymous:
                return Advertisement.objects.none()
            return self.request.user.favorites.all()

        elif self.request.user.is_superuser:
            return super().get_queryset()

        elif self.request.user.is_anonymous:
            return Advertisement.objects.exclude(draft=True)
        return Advertisement.objects.filter(Q(creator=self.request.user) | Q(draft=False))

    @action(detail=False, methods=['get'], url_path='favorite')
    def get_favorites(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(detail=True, methods=['post'], url_path='mark-as-favorite')
    def mark_as_favorite(self, request, *args, **kwargs):
        obj = self.get_object()
        self.request.user.favorites.add(obj)
        return Response({'Status': 'OK'})
