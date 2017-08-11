from teryt_tree.models import JednostkaAdministracyjna
from django_filters.filters import ModelChoiceFilter
from django.utils.translation import ugettext as _


class AreaFilter(ModelChoiceFilter):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', _("Area"))
        required = kwargs.pop('required', False)
        queryset = kwargs.pop('queryset', JednostkaAdministracyjna.objects.all())
        action = kwargs.pop('method', lambda q, _, v: q.area(v))
        super(ModelChoiceFilter, self).__init__(*args,
                                                label=label,
                                                required=required,
                                                queryset=queryset,
                                                method=action,
                                                **kwargs)


class VoivodeshipFilter(AreaFilter):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', _("Voivodeship"))
        queryset = kwargs.pop('queryset', JednostkaAdministracyjna.objects.voivodeship().all())
        super(VoivodeshipFilter, self).__init__(*args, label=label, queryset=queryset, **kwargs)


class CountyFilter(AreaFilter):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', _("County"))
        queryset = kwargs.pop('queryset', JednostkaAdministracyjna.objects.county().all())
        super(CountyFilter, self).__init__(*args, label=label, queryset=queryset, **kwargs)


class CommunityFilter(AreaFilter):
    def __init__(self, *args, **kwargs):
        label = kwargs.pop('label', _("Community"))
        queryset = kwargs.pop('queryset', JednostkaAdministracyjna.objects.community().all())
        super(CommunityFilter, self).__init__(*args, label=label, queryset=queryset, **kwargs)
