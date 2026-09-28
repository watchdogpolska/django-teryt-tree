=============================
django-teryt-tree
=============================

.. image:: https://badge.fury.io/py/django-teryt-tree.png
    :target: https://badge.fury.io/py/django-teryt-tree

.. image:: https://coveralls.io/repos/ad-m/django-teryt-tree/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ad-m/django-teryt-tree?branch=master 

Django-teryt-tree is a Django app that implements TERYT database as tree by django-mptt and flat SIMC database.

Documentation
-------------

The full documentation is at https://django-teryt-tree.readthedocs.org.

Quickstart
----------

Install django-teryt-tree::

    pip install django-teryt-tree


Then add to INSTALLED_APPS::

    INSTALLED_APPS+=('teryt_tree')

Then use it in a project::

    import teryt_tree

or::

    from teryt_tree.models import JednostkaAdministracyjna

To load TERC register database visit http://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default to download valid database. Next to execute following commands::

    pip install lxml
    python manage.py load_terc --input TERC.xml

To load SIMC register download valid database. Next to execute following commands::

    python manage.py load_simc --input SIMC.xml

Both commands accept a ``--limit`` option to cap the number of imported rows
(useful for a quick smoke test) and a ``--no-progress`` flag to disable the
progress bar, e.g.::

    python manage.py load_terc --input TERC.xml --limit 100

Usage
-----

``JednostkaAdministracyjna`` (Polish for "unit of administrative division")
stores the TERC tree of voivodeships, counties and communities using
django-mptt. ``SIMC`` stores localities and points back to the community
they belong to::

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

Features
--------

* Import database from official exports - TERC and SIMC database.
* Store data as modified pre-order traversal tree for effective regional query
* Support format of teryt.stat.gov.pl and eteryt.stat.gov.pl

For more real-world usage examples, see how the library is used in
`feder <https://github.com/watchdogpolska/feder/tree/master/feder/teryt>`_
and in `poradnia <https://github.com/watchdogpolska/poradnia/pull/645>`_.

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
