from __future__ import absolute_import

import factory
from teryt_tree import models


class CategoryFactory(factory.django.DjangoModelFactory):
    level = 1
    name = factory.Sequence(lambda n: 'category-{0}'.format(n))

    class Meta:
        model = models.Category


class JednostkaAdministracyjnaFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'jst-{0}'.format(n))
    pk = factory.Sequence(lambda n: n)
    category = factory.SubFactory(CategoryFactory)
    updated_on = '2015-05-12'
    active = True
    rght = 0
    level = 0

    class Meta:
        model = models.JednostkaAdministracyjna


def factory_jst():
    return JednostkaAdministracyjnaFactory()
