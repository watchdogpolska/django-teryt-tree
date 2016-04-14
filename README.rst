=============================
django-teryt-tree
=============================

.. image:: https://badge.fury.io/py/django-teryt-tree.png
    :target: https://badge.fury.io/py/django-teryt-tree

.. image:: https://travis-ci.org/ad-m/django-teryt-tree.png?branch=master
    :target: https://travis-ci.org/ad-m/django-teryt-tree

.. image:: https://coveralls.io/repos/ad-m/django-teryt-tree/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ad-m/django-teryt-tree?branch=master 

.. image:: https://travis-ci.org/ad-m/django-teryt-tree.svg?branch=master
    :target: https://travis-ci.org/ad-m/django-teryt-tree

Django-teryt-tree is a Django app that implements TERYT database as tree by django-mptt.

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

To load TERC register database::

    wget "http://www.stat.gov.pl/broker/access/prefile/downloadPreFile.jspa?id=1110" -O TERC.xml.zip
    unzip TERC.xml.zip
    pip install lxml
    python manage.py load_teryt TERC.xml
    rm TERC.xml*

or one-line::

    wget "http://www.stat.gov.pl/broker/access/prefile/downloadPreFile.jspa?id=1110"  -o /dev/null -O - | unzip -p - TERC.xml | python manage.py load_teryt -

Features
--------

* TODO

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
