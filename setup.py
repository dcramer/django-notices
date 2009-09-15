#!/usr/bin/env python

from setuptools import setup, find_packages

import django_notices

setup(
    name='django-notices',
    version=".".join(map(str, django_notices.__version__)),
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-notices',
    install_requires=['django'],
    description = 'A message notification system for Django.',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
