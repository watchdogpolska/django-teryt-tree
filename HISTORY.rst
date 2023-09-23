.. :changelog:

History
-------

0.18.1 (2023-09-24)
*******************

* Integrate pyproject.toml

0.18.0 (2023-09-04)
*******************

* Add support for Django 4.1, 4.2
* Drop support Django 2.2, 3.0
* Drop support Python 3.6, 3.7
* Add support Python 3.10, 3.11
* Fix deprecation warning for `django.utils.translation.ugettext_lazy`
* Fix deprecation warning for defines `default_app_config`
* Fix resource leak in tests

0.17.0 (2020-11-03)
*******************

* Add support for MultipleChoice filters in ``dal_ext``
* Add unit tests for ``dal_ext``
* Expose area queryset filters as static methods.

0.16.3 (2020-06-30)
*******************

* Fix `pk` in `JednostkaAdministracyjnaFactor` to use text
* Add '--limit' parameter to 'load_terc' command

0.16.2 (2020-06-19)
*******************

* Fix progress bar for tests

0.16.1 (2020-01-07)
*******************

* Add workflows to publish on tags
* Use setuptools_scm for versionig and drop bumpversion
* Format syntax by black
* Format migrations by pyupgrade
* Add black to linter in CI
* Fix migrations chain & upgrade for Django 3.0

0.16.0 (2020-01-07)
*******************

* Drop support Django < 2.2
* Drop support Python < 3.6
* Added support Python 3.6, 3.7, 3.8

0.15.1 (2019-10-21)
*******************

* Compatibility with Django 2.1, 2.2
* Move CI to GitHub Actions

0.14.0 (2017-08-15)
*******************

* Fix update of SIMC registry
* Fix compatibility of ``teryt_tree.est_framework_ext.viewsets.JednostkaAdministracyjnaFilter``
* Add new format od TERC export

0.13.2 (2017-08-11)
*******************

* Temporary drom SIMCSerializer

0.13.1 (2017-08-11)
*******************

* Fix django-filters compatibility in ``dal_ext``.

0.13.0 (2017-07-13)
*******************

* Improve import performance
* Add support to SIMC database
* Fix path of ```*.xml``` files (use on-premise TravisCI-cached copy)

0.12.1 (2017-04-04)
*******************

* Improve compatibility django-filters 1.x in ``dal_ext``

0.12.0 (2017-04-04)
+++++++++++++++++++

* Move ``teryt_tree.filters`` to ``teryt_tree.filters_ext.filters``
* Fix compatibility django-filters 1.x in ```filters_ext``

0.11.0 (2016-09-13)
+++++++++++++++++++
* Add locale to package

0.10.0 (2016-09-13)
+++++++++++++++++++
* Add missing migrations
* Add dummy urlpatterns

0.9.0 (2016-09-13)
++++++++++++++++++
* Fix runtests

0.8.0 (2016-12-10)
++++++++++++++++++
* Add bumpversion
* Add AppConfig with translation ``app_label``
* Update polish locale
* Extract settings as standalone file
* Add manage.py

0.7.0 (2016-09-13)
++++++++++++++++++
* Drop django 1.7 support
* Add support django 1.10
* Add ``--limit`` param to ``load_teryt`` command

0.6.0 (2016-07-03)
++++++++++++++++++

* Add django-rest-framework extensions
* Add django-autocomplete-light v3 support
* Add JednostkaAdministracyjnaQuerySet.area
* Add one-line TERC import command
* Add cache to Travis
* Fix syntax in HISTORY.rst


0.5.0 (2016-04-14)
++++++++++++++++++

* Added TravisCI badge in README.rst
* Added download_url in setup.py

0.4.0 (2016-04-14)
++++++++++++++++++

* Remove PassThroughManagerMixin

0.1.0 (2015-10-02)
++++++++++++++++++

* First release on PyPI.
