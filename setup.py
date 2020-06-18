#!/usr/bin/env python

from setuptools import setup

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="django-teryt-tree",
    description="Django-teryt-tree is a Django app that implements TERYT database as tree by django-mptt.",
    long_description=readme + "\n\n" + history,
    author="Adam Dobrawy",
    author_email="naczelnik@jawnosc.tk",
    url="https://github.com/ad-m/django-teryt-tree",
    packages=["teryt_tree"],
    include_package_data=True,
    use_scm_version=True,
    setup_requires=["setuptools_scm", "wheel"],
    install_requires=["django-mptt", "django-model-utils", "django-autoslug", "tqdm"],
    download_url="https://github.com/ad-m/django-teryt-tree/",
    license="BSD",
    zip_safe=False,
    keywords="django-teryt-tree",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Polish",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
