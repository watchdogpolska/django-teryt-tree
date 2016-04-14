#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import teryt_tree

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = teryt_tree.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-teryt-tree',
    version=version,
    description="Django-teryt-tree is a Django app that implements TERYT database as tree by django-mptt.",
    long_description=readme + '\n\n' + history,
    author='Adam Dobrawy',
    author_email='naczelnik@jawnosc.tk',
    url='https://github.com/ad-m/django-teryt-tree',
    packages=[
        'teryt_tree',
    ],
    include_package_data=True,
    install_requires=[
        'django-mptt',
        'django-model-utils',
        'django-autoslug',
        'factory-boy',
    ],
    download_url='https://github.com/ad-m/django-teryt-tree/tarball/%s' % (version),
    license="BSD",
    zip_safe=False,
    keywords='django-teryt-tree',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
