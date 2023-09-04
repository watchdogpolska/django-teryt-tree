from autocomplete_light import shortcuts as autocomplete_light
from django.utils.encoding import force_str

from .models import JednostkaAdministracyjna


class JednostkaAdministracyjnaAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ["name"]


autocomplete_light.register(
    JednostkaAdministracyjna, JednostkaAdministracyjnaAutocomplete
)


class CommunityAutocomplete(JednostkaAdministracyjnaAutocomplete):
    def choice_label(self, choice):
        return "{parent} > {choice}".format(
            parent=force_str(choice.parent), choice=force_str(choice)
        )

    def choices_for_request(self):
        self.choices = self.choices.filter(category__level=3).select_related("parent")
        return super().choices_for_request()


autocomplete_light.register(JednostkaAdministracyjna, CommunityAutocomplete)
