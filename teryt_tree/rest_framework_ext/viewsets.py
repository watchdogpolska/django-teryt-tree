import django_filters
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

try:
    from django_filters import rest_framework as filters
except ImportError:  # Back-ward compatible for django-rest-framework<3.7
    from rest_framework import filters
from rest_framework import viewsets
from teryt_tree.models import JednostkaAdministracyjna
from teryt_tree.rest_framework_ext.serializers import \
    JednostkaAdministracyjnaSerializer


def custom_area_filter(queryset, _, value):
    if not value:
        return queryset
    return queryset.area(get_object_or_404(JednostkaAdministracyjna, pk=value))


class JednostkaAdministracyjnaFilter(filters.FilterSet):
    area = django_filters.CharFilter(
        method=custom_area_filter,
        label=_("Area")
    )

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
