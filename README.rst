=============================
django-teryt-tree
=============================

.. image:: https://badge.fury.io/py/django-teryt-tree.png
    :target: https://badge.fury.io/py/django-teryt-tree

.. image:: https://travis-ci.org/ad-m/django-teryt-tree.png?branch=master
    :target: https://travis-ci.org/ad-m/django-teryt-tree

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


Then add to INSTALLEDA__APPS::

    INSTALLED_APPS+=('teryt_tree')

Then use it in a project::

    import teryt_tree

or::

    from teryt_tree.models import JednostkaAdministracyjna

To load TERC register database visit http://eteryt.stat.gov.pl/eTeryt/rejestr_teryt/udostepnianie_danych/baza_teryt/uzytkownicy_indywidualni/pobieranie/pliki_pelne.aspx?contrast=default to download valid database. Next to execute following commands::

    pip install lxml
    python manage.py load_teryt --input TERC.xml

To load SIMC register download valid database. Next to execute following commands::

    python manage.py load_simc --input SIMC.xml

Features
--------

* Import database from official exports - TERC and SIMC database.
* Store data as modified pre-order traversal tree for effective regional query
* Support format of teryt.stat.gov.pl and eteryt.stat.gov.pl

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
