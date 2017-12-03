# -*- coding: utf-8 -*-
import argparse
from itertools import islice

from tqdm import tqdm
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.lru_cache import lru_cache

try:
    from lxml import etree
except ImportError:
    raise CommandError('Missing dependency. Please, install lxml>=2.3.3')

from teryt_tree.models import Category, JednostkaAdministracyjna


class Command(BaseCommand):
    help = 'Creates a data in database base on TERC.xml file.'
    PARENT_REDUCE = {2: 0,
                     4: 2,
                     7: 4}
    LEVEL_REDUCE = {2: 1,
                    4: 2,
                    7: 3}
    FORMAT_MAP = {'nazwa_dod': 'nazdod'}

    def add_arguments(self, parser):
        parser.add_argument('--input', type=argparse.FileType('r'), nargs='?', help="Input XML-file")
        parser.add_argument('--old-format', dest='old_format', action='store_true',
                            help="Use format data of teryt.stat.gov.pl")
        parser.add_argument('--no-progress', dest='no_progress', action='store_false')

    def to_object(self, row, old_format):
        if old_format:
            data = {x.get('name').lower(): x.text for x in row}
        else:
            data = {self.FORMAT_MAP.get(x.tag.lower(), x.tag.lower()): (x.text or "").strip()
                    for x in row}
        obj = JednostkaAdministracyjna()
        obj.active = True
        obj.id = "".join(data.get(x) or '' for x in ('woj', 'pow', 'gmi', 'rodz'))
        index = len(obj.pk)
        if len(obj.id) > 2:
            obj.parent_id = obj.id[:self.PARENT_REDUCE[index]]
        obj.name = data['nazwa'].title()
        obj.updated_on = data['stan_na']
        obj.category = self.get_genre(data['nazdod'], self.LEVEL_REDUCE[index])
        return obj

    @lru_cache()
    def get_genre(self, name, level):
        obj, _ = Category.objects.get_or_create(name=name, defaults={'level': level})
        return obj

    def handle(self, no_progress, input, old_format, *args, **options):
        root = etree.parse(input)
        self.stdout.write(("Importing started. This may take a few seconds. Please wait a moment.\n"))
        with transaction.atomic():
            with JednostkaAdministracyjna.objects.delay_mptt_updates():
                for row in self.get_iter(root.iter('row'), no_progress):
                    item = self.to_object(row, old_format)
                    item.save()

    def get_iter(self, items, no_progress):
        return tqdm(items) if no_progress else items
