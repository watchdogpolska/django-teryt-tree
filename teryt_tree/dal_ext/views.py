from __future__ import unicode_literals
from dal import autocomplete
from teryt_tree.models import JednostkaAdministracyjna
from django.utils import six


class VoivodeshipAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = JednostkaAdministracyjna.objects.voivodeship().all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class CountyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = JednostkaAdministracyjna.objects.county().all()

        voivodeship = self.forwarded.get('voivodeship', None)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        if voivodeship:
            return qs.filter(parent=voivodeship)
        return qs.none()


class CommunityAutocomplete(autocomplete.Select2QuerySetView):
    def get_result_label(self, result):
        return "%s (%s)" % (six.text_type(result), six.text_type(result.category))

    def get_queryset(self):
        qs = JednostkaAdministracyjna.objects.community().select_related('category').all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        county = self.forwarded.get('county', None)
        if county:
            return qs.filter(parent=county)
        return qs.none()
