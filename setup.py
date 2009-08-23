#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-notices',
    version='0.1',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/django-notices',
    install_requires=['django'],
    description = 'A message notification system for Django.',
    packages=find_packages(),
    include_package_data=True,
)
