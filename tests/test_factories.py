from teryt_tree import factories
from django.test import TestCase


class JednostkaAdministracyjnaFactoryTestCase(TestCase):
    def test_parent_settings(self):
        obj1 = factories.JednostkaAdministracyjnaFactory()
        obj2 = factories.JednostkaAdministracyjnaFactory(parent=obj1)
        self.assertEqual(obj1.level, 0)
        self.assertEqual(obj2.level, 1)
        self.assertEqual(obj2.parent, obj1)
