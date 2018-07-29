from setuptools import find_packages
from setuptools import setup

from django_nyt import __version__


packages = find_packages()

setup(
    name="django-nyt",
    version=__version__,
    author="Benjamin Bach",
    author_email="benjamin@overtag.dk",
    url="https://github.com/benjaoming/django-nyt",
    description="A pluggable notification system written for the Django framework.",
    license="Apache License 2.0",
    keywords=["django", "notification" "alerts"],
    packages=find_packages(),
    zip_safe=False,
    install_requires=["django>=1.11,<2.1"],
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
)
