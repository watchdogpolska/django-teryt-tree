import io
import tempfile
import zipfile
from collections import OrderedDict
from os import path

from django.core import management
from django.test import TestCase


class TestParseCommand(TestCase):
    url_tmpl = 'http://www.stat.gov.pl/broker/access/prefile/'\
               'downloadPreFile.jspa?id={}'

    files = OrderedDict([
        ('TERC.xml', '1110'),
    ])

    @staticmethod
    def _get_url(url):
        try:  # Python 3.x
            import urllib.request
            response = urllib.request.urlopen(url)
        except ImportError:  # Python 2.x
            import urllib2
            response = urllib2.urlopen(url)
        return response.read()

    def _save_file(self, filename, url):
        content = self._get_url(url)
        zfile = zipfile.ZipFile(io.BytesIO(content))
        zfile.extract(filename, self.tempdir)

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        for filename, file_id in self.files.items():
            self._save_file(filename, self.url_tmpl.format(file_id))

    def test_command(self):
        for filename in self.files.keys():
            management.call_command('load_teryt', path.join(self.tempdir, filename))
