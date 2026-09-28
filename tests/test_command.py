import os
import tempfile

from django.core.management import call_command
from django.test import TestCase

from teryt_tree.models import JednostkaAdministracyjna

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


TERC_XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<data>
{rows}
</data>
"""

TERC_ROW_TEMPLATE = """<row>
<WOJ>{woj}</WOJ>
<POW></POW>
<GMI></GMI>
<RODZ></RODZ>
<NAZWA>{nazwa}</NAZWA>
<NAZWA_DOD>wojewodztwo</NAZWA_DOD>
<STAN_NA>2020-01-01</STAN_NA>
</row>
"""


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
        if not os.path.exists(filepath):
            print("Download to file {}\n".format(filepath))
            with open(filepath, "wb") as fp:
                fp.write(self._get_url(self.data_url[kind]))
                fp.flush()
        else:
            print("Reuse file {}\n".format(filepath))
        return filepath

    def test_load_commands_for_old_format(self):
        call_command(
            "load_terc",
            "--old-format",
            "--input",
            self.download_file("TERC_old.xml"),
            "--no-progress",
            stdout=StringIO(),
        )

        call_command(
            "load_simc",
            "--old-format",
            "--input",
            self.download_file("SIMC_old.xml"),
            "--no-progress",
            stdout=StringIO(),
        )

    def test_load_commands_for_current_format(self):

        call_command(
            "load_terc",
            "--input",
            self.download_file("TERC.xml"),
            "--no-progress",
            stdout=StringIO(),
        )
        call_command(
            "load_simc",
            "--input",
            self.download_file("SIMC.xml"),
            "--no-progress",
            stdout=StringIO(),
        )


class TestLoadTercDeactivation(TestCase):
    def write_terc_file(self, wojs):
        rows = "".join(
            TERC_ROW_TEMPLATE.format(woj=woj, nazwa="Region {}".format(woj))
            for woj in wojs
        )
        fp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".xml", delete=False, encoding="utf-8"
        )
        fp.write(TERC_XML_TEMPLATE.format(rows=rows))
        fp.close()
        self.addCleanup(os.unlink, fp.name)
        return fp.name

    def load_terc(self, wojs):
        call_command(
            "load_terc",
            "--input",
            self.write_terc_file(wojs),
            "--no-progress",
            stdout=StringIO(),
        )

    def test_units_missing_from_new_import_are_deactivated(self):
        self.load_terc(["02", "04"])
        self.assertTrue(JednostkaAdministracyjna.objects.get(id="02").active)
        self.assertTrue(JednostkaAdministracyjna.objects.get(id="04").active)

        self.load_terc(["02"])

        self.assertTrue(JednostkaAdministracyjna.objects.get(id="02").active)
        self.assertFalse(JednostkaAdministracyjna.objects.get(id="04").active)

    def test_reappearing_unit_is_reactivated(self):
        self.load_terc(["02", "04"])
        self.load_terc(["02"])
        self.assertFalse(JednostkaAdministracyjna.objects.get(id="04").active)

        self.load_terc(["02", "04"])

        self.assertTrue(JednostkaAdministracyjna.objects.get(id="04").active)

    def test_truncated_import_does_not_deactivate_missing_units(self):
        self.load_terc(["02", "04"])

        call_command(
            "load_terc",
            "--input",
            self.write_terc_file(["02", "06", "08"]),
            "--no-progress",
            "--limit",
            "2",
            stdout=StringIO(),
        )

        # The file has 3 rows but --limit cut it to 2, so "04" was never
        # seen in this run and must not be deactivated.
        self.assertTrue(JednostkaAdministracyjna.objects.get(id="04").active)
