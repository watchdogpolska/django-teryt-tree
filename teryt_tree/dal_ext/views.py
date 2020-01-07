from dal import autocomplete
from teryt_tree.models import JednostkaAdministracyjna


class VoivodeshipAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = JednostkaAdministracyjna.objects.voivodeship().all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class CountyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = JednostkaAdministracyjna.objects.county().all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        voivodeship = self.forwarded.get("voivodeship", None)
        if voivodeship:
            return qs.filter(parent=voivodeship)
        return qs


class CommunityAutocomplete(autocomplete.Select2QuerySetView):
    def get_result_label(self, result):
        return "{} ({})".format(str(result), str(result.category))

    def get_queryset(self):
        qs = (
            JednostkaAdministracyjna.objects.community()
            .select_related("category")
            .all()
        )

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        county = self.forwarded.get("county", None)
        if county:
            return qs.filter(parent=county)
        return qs
