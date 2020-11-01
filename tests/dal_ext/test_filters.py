from django.test import TestCase
from django_filters.filterset import FilterSet

from teryt_tree import factories
from teryt_tree.dal_ext import filters

from ..models import TestModel


class F(FilterSet):
    """
    FilterSet built on top of filters under test.
    Based on https://github.com/carltongibson/django-filter/blob/master/tests/test_filtering.py
    """

    area = filters.AreaFilter()

    class Meta:
        model = TestModel
        fields = ["area"]


class FMulti(FilterSet):
    area = filters.AreaMultipleFilter()

    class Meta:
        model = TestModel
        fields = ["area"]


class AreaFilterTestCase(TestCase):
    def setUp(self):
        self.jst_1 = factories.JednostkaAdministracyjnaFactory()
        self.jst_1_child = factories.JednostkaAdministracyjnaFactory(parent=self.jst_1)
        self.jst_2 = factories.JednostkaAdministracyjnaFactory()
        self.model_1 = TestModel.objects.create(area=self.jst_1)
        self.model_1_child = TestModel.objects.create(area=self.jst_1_child)
        self.model_2 = TestModel.objects.create(area=self.jst_2)

    def assertQsIdsEqual(self, qs, objects):
        return self.assertQuerysetEqual(
            qs, [o.pk for o in objects], lambda o: o.pk, ordered=False
        )

    def test_filter_no_params(self):
        qs = TestModel.objects.all()
        f = F({}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [self.model_1, self.model_1_child, self.model_2])

    def test_filter_single_with_child(self):
        qs = TestModel.objects.all()
        f = F({"area": self.jst_1.pk}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [self.model_1, self.model_1_child])

    def test_filter_unknown_id(self):
        qs = TestModel.objects.all()
        f = F({"area": -1}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [self.model_1, self.model_1_child, self.model_2])


class AreaMultipleFilterTestCase(TestCase):
    def setUp(self):
        self.jst_1 = factories.JednostkaAdministracyjnaFactory()
        self.jst_1_child = factories.JednostkaAdministracyjnaFactory(parent=self.jst_1)
        self.jst_2 = factories.JednostkaAdministracyjnaFactory()
        self.model_1 = TestModel.objects.create(area=self.jst_1)
        self.model_1_child = TestModel.objects.create(area=self.jst_1_child)
        self.model_2 = TestModel.objects.create(area=self.jst_2)

    def assertQsIdsEqual(self, qs, objects):
        return self.assertQuerysetEqual(
            qs, [o.pk for o in objects], lambda o: o.pk, ordered=False
        )

    def test_filter_no_params(self):
        qs = TestModel.objects.all()
        f = FMulti({}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [])

    def test_filter_no_ids(self):
        qs = TestModel.objects.all()
        f = FMulti({"area": []}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [])

    def test_filter_single_with_child(self):
        qs = TestModel.objects.all()
        f = FMulti({"area": [self.jst_1.pk]}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [self.model_1, self.model_1_child])

    def test_filter_multiple(self):
        qs = TestModel.objects.all()
        f = FMulti({"area": [self.jst_1.pk, self.jst_2.pk]}, queryset=qs)
        self.assertQsIdsEqual(f.qs, [self.model_1, self.model_1_child, self.model_2])
