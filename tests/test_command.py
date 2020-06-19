import os
import tempfile

from django.core.management import call_command
from django.test import TestCase

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


class TestCommand(TestCase):
    data_url = {
        "TERC_old.xml": "http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/TERC.xml",
        "SIMC_old.xml": "http://cdn.files.jawne.info.pl/public_html/2017/07/13_01_48_33/SIMC.xml",
        "TERC.xml": "http://cdn.files.jawne.info.pl/public_html/2017/12/03_05_43_05/TERC_Urzedowy_2017-12-03.xml",
        "SIMC.xml": "http://cdn.files.jawne.info.pl/public_html/2017/12/03_05_43_05/SIMC_Urzedowy_2017-12-03.xml",
    }
    cache_dir = os.environ.get("CACHE_DIR", tempfile.gettempdir())

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
        filepath = os.path.join(self.cache_dir, kind)
        if os.path.exists(filepath):
            print("Reuse file {}\n".format(filepath))
            return open(filepath, "rb")
        fp = open(filepath, "wb")
        print("Download to file {}\n".format(filepath))
        fp.write(self._get_url(self.data_url[kind]))
        fp.flush()
        return fp

    def test_load_commands_for_old_format(self):
        fp = self.download_file("TERC_old.xml")

        call_command(
            "load_terc",
            "--old-format",
            "--input",
            fp.name,
            "--no-progress",
            stdout=StringIO(),
        )

        fp = self.download_file("SIMC_old.xml")
        call_command(
            "load_simc",
            "--old-format",
            "--input",
            fp.name,
            "--no-progress",
            stdout=StringIO(),
        )

    def test_load_commands_for_current_format(self):
        fp = self.download_file("TERC.xml")

        call_command(
            "load_terc", "--input", fp.name, "--no-progress", stdout=StringIO()
        )

        fp = self.download_file("SIMC.xml")
        call_command(
            "load_simc", "--input", fp.name, "--no-progress", stdout=StringIO()
        )
