========
Usage
========

To use django-teryt-tree in a project::

    import teryt_tree

Loading data
------------

Download the TERC and SIMC registers from
http://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default
and load them with the bundled management commands::

    pip install lxml
    python manage.py load_terc --input TERC.xml
    python manage.py load_simc --input SIMC.xml

Both commands accept ``--limit`` (cap the number of imported rows) and
``--no-progress`` (disable the progress bar).

Querying the data
------------------

``JednostkaAdministracyjna`` stores the TERC tree of voivodeships, counties
and communities using django-mptt. ``SIMC`` stores localities and points
back to the community they belong to::

    from teryt_tree.models import JednostkaAdministracyjna, SIMC

    # Look up a unit by its TERC id
    warszawa = JednostkaAdministracyjna.objects.get(id='1465011')

    # Filter by administrative level
    JednostkaAdministracyjna.objects.voivodeship()  # level 1
    JednostkaAdministracyjna.objects.county()       # level 2
    JednostkaAdministracyjna.objects.community()    # level 3

    # Walk the tree (provided by django-mptt)
    warszawa.get_ancestors()
    warszawa.get_children()
    warszawa.get_descendants()

    # All units within the area of a given unit (e.g. a voivodeship)
    JednostkaAdministracyjna.objects.area(warszawa)

    # Localities (SIMC) belonging to a unit
    SIMC.objects.filter(terc=warszawa)

For more real-world usage examples, see how the library is used in
`feder <https://github.com/watchdogpolska/feder/tree/master/feder/teryt>`_
and in `poradnia <https://github.com/watchdogpolska/poradnia/pull/645>`_.
