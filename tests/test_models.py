#!/usr/bin/env python

"""
test_django-teryt-tree
------------

Tests for `django-teryt-tree` models module.
"""

from django.test import TestCase

from teryt_tree import models

from django.utils.encoding import force_text


class JednostkaAdministracyjnaTestCase(TestCase):
    def test_string_representation(self):
        entry = models.JednostkaAdministracyjna(name="My entry title")
        self.assertEqual(force_text(entry), entry.name)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        entry = models.Category(name="My entry title")
        self.assertEqual(force_text(entry), entry.name)
