from teryt_tree import factory
from django.test import TestCase


class JednostkaAdministracyjnaFactoryTestCase(TestCase):
    def test_parent_settings(self):
        obj1 = factory.JednostkaAdministracyjnaFactory()
        obj2 = factory.JednostkaAdministracyjnaFactory(parent=obj1)
        self.assertEqual(obj1.level, 0)
        self.assertEqual(obj2.level, 1)
        self.assertEqual(obj2.parent, obj1)
