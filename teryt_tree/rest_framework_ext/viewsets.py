import django_filters
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from teryt_tree.models import JednostkaAdministracyjna
from teryt_tree.rest_framework_ext.serializers import JednostkaAdministracyjnaSerializer


def custom_area_filter(queryset, value):
    if not value:
        return queryset
    return queryset.area(get_object_or_404(JednostkaAdministracyjna, pk=value))


class JednostkaAdministracyjnaFilter(filters.FilterSet):
    area = django_filters.CharFilter(action=custom_area_filter)

    class Meta:
        model = JednostkaAdministracyjna
        fields = ['name', 'category', 'category__level', 'area']


class JednostkaAdministracyjnaViewSet(viewsets.ModelViewSet):
    queryset = (JednostkaAdministracyjna.objects.
                select_related('category').
                prefetch_related('children').
                all())
    serializer_class = JednostkaAdministracyjnaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = JednostkaAdministracyjnaFilter
