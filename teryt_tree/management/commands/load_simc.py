# -*- coding: utf-8 -*-
import argparse
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.lru_cache import lru_cache
from tqdm import tqdm

try:
    from lxml import etree
except ImportError:
    raise CommandError('Missing dependency. Please, install lxml>=2.3.3')

from teryt_tree.models import SIMC, JednostkaAdministracyjna


class Command(BaseCommand):
    help = 'Creates a data in database base on SIMC.xml file.'

    def add_arguments(self, parser):
        parser.add_argument('--input', nargs='?', type=argparse.FileType('r'),
                            help="Input XML-file")
        parser.add_argument('--no-progress', dest='no_progress', action='store_false')

    @lru_cache()
    def get_terc(self, terc_id):
        return JednostkaAdministracyjna.objects.get(id=terc_id)

    def to_object(self, row):
        data = {x.get('name').lower(): x.text for x in row}
        terc_id = "".join(data.get(x, '') or '' for x in ('woj', 'pow', 'gmi', 'rodz_gmi'))
        terc = self.get_terc(terc_id)
        return SIMC(id=data['sym'],
                    sym_pod_id=data['sympod'],
                    terc=terc,
                    updated_on=datetime.strptime(data['stan_na'], '%Y-%m-%d'))

    def handle(self, input, no_progress, *args, **options):
        root = etree.parse(input)
        self.stdout.write(("Importing started. This may take a few seconds. Please wait a moment.\n"))
        with transaction.atomic():
            SIMC.objects.bulk_create(map(self.to_object, self.get_iter(root.iter('row'), no_progress)))

    def get_iter(self, queryset, no_progress):
        return tqdm(queryset) if no_progress else queryset
