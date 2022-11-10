from pathlib import Path
from setuptools import find_packages, setup

from django_nyt import __version__


this_directory = Path(__file__).parent
long_description = (this_directory / 'README.rst').read_text()


setup(
    name='django-nyt',
    version=__version__,
    author='Benjamin Bach',
    description='A pluggable notification system written for the Django framework.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author_email='benjamin@overtag.dk',
    url='https://github.com/benjaoming/django-nyt',
    license='Apache License 2.0',
    keywords=['django', 'notification', 'alerts'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['django>=2.2,<4.2'],
    python_requires='>=3.5',
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
    project_urls={
        'Funding': 'https://donate.pypi.org',
        'Documentation': 'https://django-nyt.readthedocs.io/en/latest/',
        'Release notes': 'https://github.com/django-wiki/django-nyt/releases',
        'Source': 'https://github.com/django-wiki/django-nyt',
        'Tracker': 'https://github.com/django-wiki/django-nyt/issues',
    },
)
