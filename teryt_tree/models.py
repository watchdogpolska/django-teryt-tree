from autoslug import AutoSlugField

from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class JednostkaAdministracyjnaManager(TreeManager):
    def with_category(self):
        return self.select_related("category")


class JednostkaAdministracyjnaQuerySet(models.QuerySet):
    def voivodeship(self):
        return self.filter(category__level=1)

    def county(self):
        return self.filter(category__level=2)

    def community(self):
        return self.filter(category__level=3)

    def area(self, jst):
        return self.filter(tree_id=jst.tree_id, lft__range=(jst.lft, jst.rght))


class Category(models.Model):
    LEVEL = Choices(
        (1, "voivodeship", _("voivodeship")),
        (2, "county", _("county")),
        (3, "community", _("community")),
    )
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name")
    level = models.IntegerField(choices=LEVEL, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class JednostkaAdministracyjna(MPTTModel):
    id = models.CharField(max_length=7, primary_key=True)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=36)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from="name", unique=True)
    updated_on = models.DateField(verbose_name=_("Updated date"))
    active = models.BooleanField(default=False)
    objects = JednostkaAdministracyjnaManager.from_queryset(
        JednostkaAdministracyjnaQuerySet
    )()

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return reverse("teryt:details", kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Unit of administrative division")
        verbose_name_plural = _("Units of administrative division")


class SIMC(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    sym_pod = models.ForeignKey("self", blank=True, on_delete=models.CASCADE)
    terc = models.ForeignKey(JednostkaAdministracyjna, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    updated_on = models.DateField(verbose_name=_("Updated date"))

    def __str__(self):
        return "{}".format(self.name)
