Latest Changes
==============


Compiled on: Fri Apr 15 15:04:09 CEST 2016::

    *   d9d39ce - (HEAD, origin/master, origin/HEAD, master) Merge pull request #21 from benjaoming/channels (2 minutes ago) <Benjamin Bach>
    |\  
    | * 3e1d18e - (origin/channels, channels) documentation improvements (8 minutes ago) <Benjamin Bach>
    | * 251bfc0 - Use individual channels for each notification type key (9 minutes ago) <Benjamin Bach>
    | * 67c862d - Updates to settings and make SLEEP_TIME a command line option (2 days ago) <Benjamin Bach>
    | * 62d38eb - run apidocs on RTD (3 days ago) <Benjamin Bach>
    | * 2901d27 - autodocs and settings module automatically documented (3 days ago) <Benjamin Bach>
    | * c1515f4 - pep8 conf file for docs (3 days ago) <Benjamin Bach>
    | * 5bda7e2 - submit coveralls after all tox have run (3 days ago) <Benjamin Bach>
    | * 8a763f2 - use open() not file() (3 days ago) <Benjamin Bach>
    | * baa6bc4 - use new-style exceptions (3 days ago) <Benjamin Bach>
    | * e7f10fa - use new-style TEMPLATES settings for test env (3 days ago) <Benjamin Bach>
    | * 23ebb15 - automatically switch between django 1.9+ and <1.9 url patterns (3 days ago) <Benjamin Bach>
    | * d143786 - Improvements to readme (3 days ago) <Benjamin Bach>
    | * 9f5644f - add coverage inside the tox env (3 days ago) <Benjamin Bach>
    | * 135954a - rm unused import (3 days ago) <Benjamin Bach>
    | * 604d959 - pep8 migrations (3 days ago) <Benjamin Bach>
    | * dd059ce - add coveralls badge (3 days ago) <Benjamin Bach>
    | * 0648092 - use old dj 1.7 and 1.8 friendly pattern (3 days ago) <Benjamin Bach>
    | * a26687c - run coverage inside tox (3 days ago) <Benjamin Bach>
    | * 205d615 - update pattern for django admin to avoid deprecation warnings (3 days ago) <Benjamin Bach>
    | * 39c7886 - tests for management commands and new test cases for test_basic (3 days ago) <Benjamin Bach>
    | * 80a2fc4 - Move testproject to test-project to avoid testproject/testproject which raises ImportWarning (3 days ago) <Benjamin Bach>
    | * 2c1c17d - Set default on_delete=models.CASCADE because of Django 2.0 Deprecation (3 days ago) <Benjamin Bach>
    | * 1444805 - Fix #4 by having a related_name specified for external User model (4 days ago) <Benjamin Bach>
    | * e822490 - upgrade testproject dashboard (4 days ago) <Benjamin Bach>
    | * 0e62d11 - finalization of preliminary websocket support (4 days ago) <Benjamin Bach>
    | * 5f9a6ff - upgrade to production/stable status (4 days ago) <Benjamin Bach>
    | * 478a0c9 - mention channels in readme (4 days ago) <Benjamin Bach>
    | * 0e2acf0 - testproject use of channels (12 days ago) <Benjamin Bach>
    | * f1d0a89 - Initial support for channels (12 days ago) <Benjamin Bach>
    | * d6eb2df - update pypi python support meta data (12 days ago) <Benjamin Bach>
    | * 8c49f65 - fix up broken docs javascript example code (12 days ago) <Benjamin Bach>
    | * 251874b - Use functool.wraps for decorators (12 days ago) <Benjamin Bach>
    | * b3d268c - do not test dj 1.9 and py 3.3, not supported (12 days ago) <Benjamin Bach>
    | * ef467d4 - testapp to be included in tests (13 days ago) <Benjamin Bach>
    | * 05b5e33 - Cleanup after remove Dj 1.5 and 1.6 support (13 days ago) <Benjamin Bach>
    | * 1eea062 - remove dj 1.5 and 1.6 and add dj 1.9 (13 days ago) <Benjamin Bach>
    | * d6ef4ba - update tests and add missing save() call (13 days ago) <Benjamin Bach>
    | * d2edf85 - Drop python 2.6 tests (13 days ago) <Benjamin Bach>
    | * 13cb421 - First version testapp panel for testproject, emulate user login and create settings for users (13 days ago) <Benjamin Bach>
    | * 03c50d6 - Add new fields Notification.modified and Settings.is_default (13 days ago) <Benjamin Bach>
    | * 283308f - some minor pep8 stuff (13 days ago) <Benjamin Bach>
    |/  
    * 6481fd7 - have a break, have a Make.....file (7 weeks ago) <Benjamin Bach>
    * 4a89846 - (tag: alpha/0.9.9) version bump (7 weeks ago) <Benjamin Bach>
    *   bfa5e8f - Merge pull request #20 from VCAMP/master (7 weeks ago) <Benjamin Bach>
    |\  
    | * da8c2bf - Simple fix for deprecated {% load url from future %} tag (7 weeks ago) <Valerio Campanella>
    | * 336981c - Fixed Django 1.9 compatibility issue (7 weeks ago) <Valerio Campanella>
    |/  
    * 85e8fdf - fix formatting error that made the README unreadable to the PyPi rst engine (6 months ago) <Benjamin Bach>
    * e14599c - (tag: alpha/0.9.8) bump version (6 months ago) <Benjamin Bach>
    * 2cac72b - remove the long_description flutter, README.rst is automatically found by setuptools (6 months ago) <Benjamin Bach>
    * 8ab1631 - remove the long_description flutter, README.rst is automatically found by PyPi (6 months ago) <Benjamin Bach>
    * b51b9c8 - badges in one line (6 months ago) <Benjamin Bach>
    * d6e1300 - fix broken badges (6 months ago) <Benjamin Bach>
    * 981048a - remove redundant readme file (6 months ago) <Benjamin Bach>
    * 71bf5f4 - bump version to 0.9.7.3 (6 months ago) <Benjamin Bach>
    *   54433e2 - Merge pull request #18 from spookylukey/fix_django_18_url_deprecation_warning (6 months ago) <benjaoming>
    |\  
    | * adc830c - Allow Travis CI to use new container infrastructure for faster tests. (6 months ago) <Luke Plant>
    | * 2cb5537 - Fixed Travis to run tests on Django 1.8 (6 months ago) <Luke Plant>
    | * b4e8a79 - Upgraded tested Django versions (6 months ago) <Luke Plant>
    | * 0520765 - Fixed deprecation warning while running tests on Django 1.8. (6 months ago) <Luke Plant>
    | * a27e9bd - Rewrote tox.ini using new features (6 months ago) <Luke Plant>
    | * c9bc1eb - Fixed URLconf to avoid deprecation warning on Django 1.8 (6 months ago) <Luke Plant>
    | * c75e693 - Added basic test for mark_read view (6 months ago) <Luke Plant>
    |/  
    *   ec0e559 - Merge pull request #16 from tonioo/master (9 months ago) <benjaoming>
    |\  
    | * 5ca0788 - A custom User model does not always have a username field. (9 months ago) <Antoine Nguyen>
    * | 7d24c4d - remove django 1.4 from travis (9 months ago) <Benjamin Bach>
    * | 1c9c3fe - remove django 1.4 from tox (9 months ago) <Benjamin Bach>
    * | a6ca052 - Stop supporting Django 1.4 (9 months ago) <benjaoming>
    |/  
    * 7166e18 - update to beta (10 months ago) <Benjamin Bach>
    *   ed504ee - Merge pull request #14 from bargool/master (11 months ago) <benjaoming>
    |\  
    | * b1e0b23 - Changed str to encode('utf-8'). Translated string can be non-ascii. And str() raises error with python 2 (11 months ago) <Alexey Nakoryakov>
    |/  
    * f76f1e6 - and another tox typo (12 months ago) <Benjamin Bach>
    * 390634f - bump south version and fix tox syntax error (12 months ago) <Benjamin Bach>
    * d26ea10 - bump version for uploading a with signature (12 months ago) <Benjamin Bach>
    * 3e58011 - bump version (12 months ago) <Benjamin Bach>
    * c0a51e3 - remove south from requirements (12 months ago) <Benjamin Bach>
    * 891aa4b - test only with south when required (12 months ago) <Benjamin Bach>
    * 1c8602a - bump version (12 months ago) <Benjamin Bach>
    * ab5edd5 - Use list instead of patterns() (12 months ago) <Benjamin Bach>
    * 03c9cca - Fix screenshot src (12 months ago) <Benjamin Bach>
    * 80f6f98 - add django 1.8 to tests (12 months ago) <Benjamin Bach>
    * c7f7e8e - fix link of example image (1 year, 3 months ago) <Benjamin Bach>
    * 5e394b5 - re-release due to broken readme on pypi (1 year, 3 months ago) <Benjamin Bach>
    * 747e0a4 - auto-generated from README.md (1 year, 3 months ago) <Benjamin Bach>
    * 5d82b54 - do not use markdown file for descriptions (1 year, 3 months ago) <Benjamin Bach>
    * 04d0864 - badge for egg and wheel (1 year, 3 months ago) <Benjamin Bach>
    * 86e691f - Add python support details to meta data (1 year, 3 months ago) <Benjamin Bach>
    * deafa39 - add wheel support (1 year, 3 months ago) <Benjamin Bach>
    * 6c60ad6 - do not pin South, it breaks other requirements (1 year, 3 months ago) <Benjamin Bach>
    * 8602f99 - auto-generated from README.md (1 year, 3 months ago) <Benjamin Bach>
    * 85e0137 - RIP crate.io (1 year, 4 months ago) <Benjamin Bach>
    * 18084d4 - Errors and better text for the readme (1 year, 4 months ago) <Benjamin Bach>
    * de0c389 - (tag: alpha/0.9.5) bump version (1 year, 4 months ago) <Benjamin Bach>
    * b89ab6d - Removing unused .travis dir (#12) (1 year, 4 months ago) <Benjamin Bach>
    *   b99ca6d - Merge pull request #12 from spookylukey/fix_travis_and_tests (1 year, 4 months ago) <benjaoming>
    |\  
    | * 5636cfd - Fixed position of 'coding' lines (1 year, 4 months ago) <Luke Plant>
    | * cc262dd - Added tests for Django 1.7 (1 year, 4 months ago) <Luke Plant>
    | * c3a8f56 - Added missing migration. (1 year, 4 months ago) <Luke Plant>
    | * ea890b5 - Replaced testing on Python 3.2 with 3.3, because 3.2 is no longer supported by South (1 year, 4 months ago) <Luke Plant>
    | * f384336 - Removed some non-working test combinations. (1 year, 4 months ago) <Luke Plant>
    | * 1c60cc9 - Fixed South migrations on Django 1.4 (1 year, 4 months ago) <Luke Plant>
    | * 6a6e32f - Created tox.ini and fixed travis.yml to use tox. (1 year, 4 months ago) <Luke Plant>
    | * 5dccdcf - Fixed duplication and other issues in runtests.py (1 year, 4 months ago) <Luke Plant>
    |/  
    * aeaaed3 - fix #11 (1 year, 5 months ago) <benjaoming>
    * 7ec878a - Add docs about the south migrations module pr #9 (1 year, 5 months ago) <benjaoming>
    * b400a12 - Also related to #10 -- add same change to the migration script migrater (1 year, 5 months ago) <benjaoming>
    * e363fc3 - remove deprecation warnings, fix #10 (1 year, 5 months ago) <benjaoming>
    * 3b13838 - Pin south version and close #9 (1 year, 5 months ago) <valberg>
    *   04a135c - Merge pull request #8 from cXhristian/filter-exclude-fix (1 year, 5 months ago) <valberg>
    |\  
    | * d6ae60e - Fix filter_exclude (1 year, 5 months ago) <Christian Duvholt>
    |/  
    * 8ea5f4e - add get_or_create functionality to subscribe() function and fix tests to include subscribe() (1 year, 6 months ago) <benjaoming>
    * 18d8ae0 - (tag: alpha/0.9.4) Hopefully last remaining issue to close #6 - models __unicode__ replaced by __str__ (1 year, 6 months ago) <benjaoming>
    * 49efcf1 - add python 3 tests (1 year, 6 months ago) <benjaoming>
    * 3b08dbf - six required for travis (1 year, 6 months ago) <benjaoming>
    * 0b9b63d - add six to requirements (1 year, 6 months ago) <benjaoming>
    * 8b51161 - version bump (1 year, 6 months ago) <benjaoming>
    * d95bf4f - utility script for running tests (1 year, 6 months ago) <benjaoming>
    * 13b8c6c - (2to3) use python-modernize to have py2+3 compatibility (1 year, 6 months ago) <benjaoming>
    *   08d5836 - Merge pull request #7 from jluttine/finnish-translation (1 year, 6 months ago) <benjaoming>
    |\  
    | * 529402c - Preliminary Finnish translation (1 year, 6 months ago) <Jaakko Luttinen>
    |/  
    * 660f9c3 - add support for custom user models in south migrations #5 (1 year, 6 months ago) <benjaoming>
    *   367125b - Merge pull request #3 from destos/master (1 year, 7 months ago) <benjaoming>
    |\  
    | * d775f6e - use content_type over depreciated mimetype (1 year, 7 months ago) <Patrick Forringer>
    |/  
    *   b40ddf9 - Merge pull request #2 from holoduke/master (1 year, 7 months ago) <benjaoming>
    |\  
    | * 2be7afa - Update models.py (1 year, 8 months ago) <Gillis Haasnoot>
    |/  
    * 50af164 - goto should return to referer when url is empty string (1 year, 9 months ago) <benjaoming>
    * 60e3582 - Version bump (1 year, 9 months ago) <benjaoming>
    * 4942b2a - fix total_count going to 0 (1 year, 9 months ago) <benjaoming>
    * cf0cc32 - Return None for key type on direct notifications (1 year, 9 months ago) <benjaoming>
    * e815a58 - Fix setting user from subscription.settings (1 year, 9 months ago) <benjaoming>
    * cb721b2 - do not use simplejson (1 year, 9 months ago) <benjaoming>
    * 2940669 - str representation for Notification should use user field (1 year, 9 months ago) <benjaoming>
    * e1fad6d - make notifications without subscriptions possible in views (1 year, 9 months ago) <benjaoming>
    * 4b2cbeb - raw_id_fields for big model relations (1 year, 9 months ago) <benjaoming>
    * f56781d - (tag: alpha/0.9.2) version bump (1 year, 9 months ago) <benjaoming>
    * 08c9f8e - new subscribe() utility method (1 year, 9 months ago) <benjaoming>
    * d26f8f7 - improve database layout, add NotificationType.get_by_key (1 year, 9 months ago) <benjaoming>
    * f97b7d6 - danish translation (1 year, 9 months ago) <benjaoming>
    * 0315f6e - autopep8 (1 year, 9 months ago) <benjaoming>
    * 2b88391 - version bump + deprecate using django_nyt.notify, should be django_nyt.utils.notify (1 year, 11 months ago) <benjaoming>
    * d0243f7 - 2to3 patch (1 year, 11 months ago) <benjaoming>
    * e9e2254 - remove pattern causing setup.py warnings (1 year, 11 months ago) <benjaoming>
    * 91f9a1b - remove old style test module (1 year, 11 months ago) <benjaoming>
    * 09f0f21 - Refactor test project settings to work with newest django (and old as well) (1 year, 11 months ago) <benjaoming>
    * 5df2e23 - Move old south migrations to south_migraitons module (1 year, 11 months ago) <benjaoming>
    * c780cc4 - Add compat layer, move notify to utils.notify, add first test case (1 year, 11 months ago) <benjaoming>
    * d4da17e - Documentation change for django_nyt.utils.notify (1 year, 11 months ago) <benjaoming>
    * 9a3f383 - rename default url subtree (1 year, 11 months ago) <benjaoming>
    * 641063f - pep8 setup.py + readme changes (1 year, 11 months ago) <benjaoming>
    * 064a597 - badges in README (2 years, 3 months ago) <benjaoming>
    * cbc7e65 - fix django 1.6 test running (2 years, 3 months ago) <benjaoming>
    * 5a52509 - travis configuration (2 years, 3 months ago) <benjaoming>
    * e97d170 - README updates and travis hook (2 years, 3 months ago) <benjaoming>
    * f9a65a5 - README for PyPi, som PEP8 (2 years, 3 months ago) <benjaoming>
    * 94b7f1d - remove code block from index (2 years, 3 months ago) <benjaoming>
    * e2fc6cf - javascript and html example (2 years, 3 months ago) <benjaoming>
    * 4519c8c - change default url path, add more installation notes and configuration (2 years, 3 months ago) <benjaoming>
    * d20bac2 - Installation notes (2 years, 3 months ago) <benjaoming>
    * a15d990 - (tag: alpha/0.9) pypi release (2 years, 3 months ago) <benjaoming>
    * 9db86c4 - remove build directory (2 years, 3 months ago) <benjaoming>
    * 63106b0 - add new chapter, fix headlines (2 years, 3 months ago) <benjaoming>
    *   96538c7 - Merge branch 'master' of github.com:benjaoming/django-nyt (2 years, 3 months ago) <benjaoming>
    |\  
    | * c341040 - some rst formatting (2 years, 3 months ago) <benjaoming>
    * | 461ad64 - some rst formatting (2 years, 3 months ago) <benjaoming>
    |/  
    * cfb8c3d - add docs and shorten README (2 years, 3 months ago) <benjaoming>
    * 8224df0 - initial commit, moving files from django-wiki and refactoring from django_notify to django_nyt (2 years, 3 months ago) <benjaoming>
    * b7d616d - Initial commit (2 years, 3 months ago) <benjaoming>