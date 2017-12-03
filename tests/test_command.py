import os
import tempfile

from django.core.management import call_command
from django.test import TestCase


class TestCommand(TestCase):
    data_url = {'TERC.xml': 'http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/TERC.xml',
                'SIMC.xml': 'http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/SIMC.xml'}
    cache_dir = os.environ.get('CACHE_DIR', tempfile.gettempdir())

    @staticmethod
    def _get_url(url):
        try:  # Python 3.x
            import urllib.request
            response = urllib.request.urlopen(url)
        except ImportError:  # Python 2.x
            import urllib2
            response = urllib2.urlopen(url)
        return response.read()

    def setUp(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def download_file(self, kind):
        fp = open(os.path.join(self.cache_dir, kind), 'wb')
        fp.write(self._get_url(self.data_url[kind]))
        fp.flush()
        return fp

    def test_load_commands(self):
        fp = self.download_file('TERC.xml')

        call_command('load_terc', '--input', fp.name, '--no-progress')

        fp = self.download_file('SIMC.xml')
        call_command('load_simc', '--input', fp.name, '--no-progress')
