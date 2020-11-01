from django.db import models

from teryt_tree.models import JednostkaAdministracyjna
from teryt_tree.dal_ext.filters import AreaFilter, AreaMultipleFilter


class TestModelQuerySet(models.QuerySet):
    def area(self, jst):
        return AreaFilter.filter_area(self, jst, "area")

    def area_in(self, jst):
        return AreaMultipleFilter.filter_area_in(self, jst, "area")


class TestModel(models.Model):
    area = models.ForeignKey(JednostkaAdministracyjna, on_delete=models.CASCADE)
    objects = TestModelQuerySet.as_manager()
