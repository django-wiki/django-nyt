# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
from django_nyt import VERSION
from setuptools import setup, find_packages

def get_path(fname):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)

def read(fname):
    return open(get_path(fname)).read()

packages = find_packages()

setup(
    name="django-nyt",
    version=VERSION,
    author="Benjamin Bach",
    author_email="benjamin@overtag.dk",
    url="https://github.com/benjaoming/django-nyt",
    description="A pluggable notification system written for the Django framework.",
    license="Apache License 2.0",
    keywords=["django", "notification" "alerts"],
    packages=find_packages(exclude=["testproject", "testproject.*"]),
    zip_safe=False,
    install_requires=read('requirements.txt').split("\n"),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
)
