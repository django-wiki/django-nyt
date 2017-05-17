Latest Changes
==============


Compiled on: Wed May 17 14:59:40 CEST 2017::

    * 52a2017 - (HEAD -> master, tag: beta/1.0b3, origin/master, origin/HEAD) Release note for #33 (32 seconds ago) <Benjamin Bach>
    * d3fa54d - Bump to 1.0b3 (3 minutes ago) <Benjamin Bach>
    *   f19280d - Merge pull request #33 from ztomaz/master (4 minutes ago) <Benjamin Bach>
    |\  
    | * bc1598c - Update consumers.py (30 minutes ago) <Tomaž Žniderič>
    |/  
    * 44bd3f9 - (tag: beta/1.0b2) auto-generated HISTORY.rst for 0.1b2 (5 weeks ago) <Benjamin Bach>
    *   97975fb - Merge pull request #32 from benjaoming/dj111 (5 weeks ago) <Benjamin Bach>
    |\  
    | * d00d373 - (origin/dj111, dj111) Set option defaults django 1.10 + 1.11 (5 weeks ago) <Benjamin Bach>
    | * ed7aa6e - codecov dependency for travis.yml (5 weeks ago) <Benjamin Bach>
    | * bef96ae - Correctly set default command line options for notifymail (5 weeks ago) <Benjamin Bach>
    | * c13b02b - Replace coveralls with CodeCov.io (5 weeks ago) <Benjamin Bach>
    | * c7c97e3 - Release note for #28 - thanks @hiasen (5 weeks ago) <Benjamin Bach>
    | * b185a91 - Bump to version 0.1b2 (5 weeks ago) <Benjamin Bach>
    | * 70b92e5 - Add Django 1.11 to test matrix (5 weeks ago) <Benjamin Bach>
    |/  
    *   48fd473 - Merge pull request #28 from hiasen/str-fix (5 weeks ago) <Benjamin Bach>
    |\  
    | * d2f9450 - Fix bug with __str__ in python 3 (7 months ago) <Øystein Hiåsen>
    * | 4b78a5d - Prettify a bit of code before a demo at hackathon (6 months ago) <Benjamin Bach>
    |/  
    * d019923 - (origin/requirements-fix, requirements-fix) Add migration for new related_name and CASCADE constraints (7 months ago) <Benjamin Bach>
    * b74b90d - Specify the Python versions for Travis (8 months ago) <Benjamin Bach>
    * 05d747e - Build the full django + python matrix (8 months ago) <Benjamin Bach>
    * ac8e8a4 - Update requirements.txt to match Django>=1.7 requirement (8 months ago) <Benjamin Bach>
    * ee30f06 - Clean up (8 months ago) <Benjamin Bach>
    * 9975c13 - Auto-generated history for 1.0b1 (8 months ago) <Benjamin Bach>
    * f588f9e - Keywords should be a list (8 months ago) <Benjamin Bach>
    * 14bd12e - Correction: It's also django 1.10 compatible (8 months ago) <Benjamin Bach>
    *   ce79824 - (tag: beta/1.0b1) Merge pull request #25 from benjaoming/django110 (8 months ago) <Benjamin Bach>
    |\  
    | * b24bbf7 - Release notes about django support (8 months ago) <Benjamin Bach>
    | * c67e396 - Do not set defaults in make_option because they aren't set in Python 3.5 (8 months ago) <Benjamin Bach>
    | * b6989a3 - Fix unresolved import in django 1.10 (8 months ago) <Benjamin Bach>
    | * 2979fcd - Add django 1.10 to Tox configuration (8 months ago) <Benjamin Bach>
    | * a167397 - Add release notes docs section (8 months ago) <Benjamin Bach>
    | * d5f15ec - Fix rtd.io links and update docs requirements (8 months ago) <Benjamin Bach>
    * |   b784fc5 - Merge pull request #24 from benjaoming/celery-compat (8 months ago) <Benjamin Bach>
    |\ \  
    | |/  
    |/|   
    | * 249dfa4 - (origin/celery-compat, celery-compat) Refactor `tasks` to `subscribers` because of celery auto-loading - fixes #23 (8 months ago) <Benjamin Bach>
    |/  
    * 51b8992 - remove unused section about South support (1 year, 1 month ago) <Benjamin Bach>
    * a90a611 - add missing section on daemon (1 year, 1 month ago) <Benjamin Bach>
    * 41d806c - add requirements file with channels for RTD (1 year, 1 month ago) <Benjamin Bach>
    * ec15d2c - add note about --pre (1 year, 1 month ago) <Benjamin Bach>
    * 44e9c96 - (tag: alpha/1.0dev0) updates to make target 'release' and 'sdist' + changelog (1 year, 1 month ago) <Benjamin Bach>
    *   d9d39ce - Merge pull request #21 from benjaoming/channels (1 year, 1 month ago) <Benjamin Bach>
    |\  
    | * 3e1d18e - (origin/channels, channels) documentation improvements (1 year, 1 month ago) <Benjamin Bach>
    | * 251bfc0 - Use individual channels for each notification type key (1 year, 1 month ago) <Benjamin Bach>
    | * 67c862d - Updates to settings and make SLEEP_TIME a command line option (1 year, 1 month ago) <Benjamin Bach>
    | * 62d38eb - run apidocs on RTD (1 year, 1 month ago) <Benjamin Bach>
    | * 2901d27 - autodocs and settings module automatically documented (1 year, 1 month ago) <Benjamin Bach>
    | * c1515f4 - pep8 conf file for docs (1 year, 1 month ago) <Benjamin Bach>
    | * 5bda7e2 - submit coveralls after all tox have run (1 year, 1 month ago) <Benjamin Bach>
    | * 8a763f2 - use open() not file() (1 year, 1 month ago) <Benjamin Bach>
    | * baa6bc4 - use new-style exceptions (1 year, 1 month ago) <Benjamin Bach>
    | * e7f10fa - use new-style TEMPLATES settings for test env (1 year, 1 month ago) <Benjamin Bach>
    | * 23ebb15 - automatically switch between django 1.9+ and <1.9 url patterns (1 year, 1 month ago) <Benjamin Bach>
    | * d143786 - Improvements to readme (1 year, 1 month ago) <Benjamin Bach>
    | * 9f5644f - add coverage inside the tox env (1 year, 1 month ago) <Benjamin Bach>
    | * 135954a - rm unused import (1 year, 1 month ago) <Benjamin Bach>
    | * 604d959 - pep8 migrations (1 year, 1 month ago) <Benjamin Bach>
    | * dd059ce - add coveralls badge (1 year, 1 month ago) <Benjamin Bach>
    | * 0648092 - use old dj 1.7 and 1.8 friendly pattern (1 year, 1 month ago) <Benjamin Bach>
    | * a26687c - run coverage inside tox (1 year, 1 month ago) <Benjamin Bach>
    | * 205d615 - update pattern for django admin to avoid deprecation warnings (1 year, 1 month ago) <Benjamin Bach>
    | * 39c7886 - tests for management commands and new test cases for test_basic (1 year, 1 month ago) <Benjamin Bach>
    | * 80a2fc4 - Move testproject to test-project to avoid testproject/testproject which raises ImportWarning (1 year, 1 month ago) <Benjamin Bach>
    | * 2c1c17d - Set default on_delete=models.CASCADE because of Django 2.0 Deprecation (1 year, 1 month ago) <Benjamin Bach>
    | * 1444805 - Fix #4 by having a related_name specified for external User model (1 year, 1 month ago) <Benjamin Bach>
    | * e822490 - upgrade testproject dashboard (1 year, 1 month ago) <Benjamin Bach>
    | * 0e62d11 - finalization of preliminary websocket support (1 year, 1 month ago) <Benjamin Bach>
    | * 5f9a6ff - upgrade to production/stable status (1 year, 1 month ago) <Benjamin Bach>
    | * 478a0c9 - mention channels in readme (1 year, 1 month ago) <Benjamin Bach>
    | * 0e2acf0 - testproject use of channels (1 year, 1 month ago) <Benjamin Bach>
    | * f1d0a89 - Initial support for channels (1 year, 1 month ago) <Benjamin Bach>
    | * d6eb2df - update pypi python support meta data (1 year, 1 month ago) <Benjamin Bach>
    | * 8c49f65 - fix up broken docs javascript example code (1 year, 1 month ago) <Benjamin Bach>
    | * 251874b - Use functool.wraps for decorators (1 year, 1 month ago) <Benjamin Bach>
    | * b3d268c - do not test dj 1.9 and py 3.3, not supported (1 year, 1 month ago) <Benjamin Bach>
    | * ef467d4 - testapp to be included in tests (1 year, 1 month ago) <Benjamin Bach>
    | * 05b5e33 - Cleanup after remove Dj 1.5 and 1.6 support (1 year, 1 month ago) <Benjamin Bach>
    | * 1eea062 - remove dj 1.5 and 1.6 and add dj 1.9 (1 year, 1 month ago) <Benjamin Bach>
    | * d6ef4ba - update tests and add missing save() call (1 year, 1 month ago) <Benjamin Bach>
    | * d2edf85 - Drop python 2.6 tests (1 year, 1 month ago) <Benjamin Bach>
    | * 13cb421 - First version testapp panel for testproject, emulate user login and create settings for users (1 year, 1 month ago) <Benjamin Bach>
    | * 03c50d6 - Add new fields Notification.modified and Settings.is_default (1 year, 1 month ago) <Benjamin Bach>
    | * 283308f - some minor pep8 stuff (1 year, 1 month ago) <Benjamin Bach>
    |/  
    * 6481fd7 - have a break, have a Make.....file (1 year, 3 months ago) <Benjamin Bach>
    * 4a89846 - (tag: alpha/0.9.9) version bump (1 year, 3 months ago) <Benjamin Bach>
    *   bfa5e8f - Merge pull request #20 from VCAMP/master (1 year, 3 months ago) <Benjamin Bach>
    |\  
    | * da8c2bf - Simple fix for deprecated {% load url from future %} tag (1 year, 3 months ago) <Valerio Campanella>
    | * 336981c - Fixed Django 1.9 compatibility issue (1 year, 3 months ago) <Valerio Campanella>
    |/  
    * 85e8fdf - fix formatting error that made the README unreadable to the PyPi rst engine (1 year, 7 months ago) <Benjamin Bach>
    * e14599c - (tag: alpha/0.9.8) bump version (1 year, 7 months ago) <Benjamin Bach>
    * 2cac72b - remove the long_description flutter, README.rst is automatically found by setuptools (1 year, 7 months ago) <Benjamin Bach>
    * 8ab1631 - remove the long_description flutter, README.rst is automatically found by PyPi (1 year, 7 months ago) <Benjamin Bach>
    * b51b9c8 - badges in one line (1 year, 7 months ago) <Benjamin Bach>
    * d6e1300 - fix broken badges (1 year, 7 months ago) <Benjamin Bach>
    * 981048a - remove redundant readme file (1 year, 7 months ago) <Benjamin Bach>
    * 71bf5f4 - bump version to 0.9.7.3 (1 year, 7 months ago) <Benjamin Bach>
    *   54433e2 - Merge pull request #18 from spookylukey/fix_django_18_url_deprecation_warning (1 year, 7 months ago) <benjaoming>
    |\  
    | * adc830c - Allow Travis CI to use new container infrastructure for faster tests. (1 year, 7 months ago) <Luke Plant>
    | * 2cb5537 - Fixed Travis to run tests on Django 1.8 (1 year, 7 months ago) <Luke Plant>
    | * b4e8a79 - Upgraded tested Django versions (1 year, 7 months ago) <Luke Plant>
    | * 0520765 - Fixed deprecation warning while running tests on Django 1.8. (1 year, 7 months ago) <Luke Plant>
    | * a27e9bd - Rewrote tox.ini using new features (1 year, 7 months ago) <Luke Plant>
    | * c9bc1eb - Fixed URLconf to avoid deprecation warning on Django 1.8 (1 year, 7 months ago) <Luke Plant>
    | * c75e693 - Added basic test for mark_read view (1 year, 7 months ago) <Luke Plant>
    |/  
    *   ec0e559 - Merge pull request #16 from tonioo/master (1 year, 10 months ago) <benjaoming>
    |\  
    | * 5ca0788 - A custom User model does not always have a username field. (1 year, 10 months ago) <Antoine Nguyen>
    * | 7d24c4d - remove django 1.4 from travis (1 year, 10 months ago) <Benjamin Bach>
    * | 1c9c3fe - remove django 1.4 from tox (1 year, 10 months ago) <Benjamin Bach>
    * | a6ca052 - Stop supporting Django 1.4 (1 year, 10 months ago) <benjaoming>
    |/  
    * 7166e18 - update to beta (1 year, 10 months ago) <Benjamin Bach>
    *   ed504ee - Merge pull request #14 from bargool/master (1 year, 11 months ago) <benjaoming>
    |\  
    | * b1e0b23 - Changed str to encode('utf-8'). Translated string can be non-ascii. And str() raises error with python 2 (2 years ago) <Alexey Nakoryakov>
    |/  
    * f76f1e6 - and another tox typo (2 years, 1 month ago) <Benjamin Bach>
    * 390634f - bump south version and fix tox syntax error (2 years, 1 month ago) <Benjamin Bach>
    * d26ea10 - bump version for uploading a with signature (2 years, 1 month ago) <Benjamin Bach>
    * 3e58011 - bump version (2 years, 1 month ago) <Benjamin Bach>
    * c0a51e3 - remove south from requirements (2 years, 1 month ago) <Benjamin Bach>
    * 891aa4b - test only with south when required (2 years, 1 month ago) <Benjamin Bach>
    * 1c8602a - bump version (2 years, 1 month ago) <Benjamin Bach>
    * ab5edd5 - Use list instead of patterns() (2 years, 1 month ago) <Benjamin Bach>
    * 03c9cca - Fix screenshot src (2 years, 1 month ago) <Benjamin Bach>
    * 80f6f98 - add django 1.8 to tests (2 years, 1 month ago) <Benjamin Bach>
    * c7f7e8e - fix link of example image (2 years, 4 months ago) <Benjamin Bach>
    * 5e394b5 - re-release due to broken readme on pypi (2 years, 4 months ago) <Benjamin Bach>
    * 747e0a4 - auto-generated from README.md (2 years, 4 months ago) <Benjamin Bach>
    * 5d82b54 - do not use markdown file for descriptions (2 years, 4 months ago) <Benjamin Bach>
    * 04d0864 - badge for egg and wheel (2 years, 4 months ago) <Benjamin Bach>
    * 86e691f - Add python support details to meta data (2 years, 4 months ago) <Benjamin Bach>
    * deafa39 - add wheel support (2 years, 4 months ago) <Benjamin Bach>
    * 6c60ad6 - do not pin South, it breaks other requirements (2 years, 4 months ago) <Benjamin Bach>
    * 8602f99 - auto-generated from README.md (2 years, 4 months ago) <Benjamin Bach>
    * 85e0137 - RIP crate.io (2 years, 5 months ago) <Benjamin Bach>
    * 18084d4 - Errors and better text for the readme (2 years, 5 months ago) <Benjamin Bach>
    * de0c389 - (tag: alpha/0.9.5) bump version (2 years, 5 months ago) <Benjamin Bach>
    * b89ab6d - Removing unused .travis dir (#12) (2 years, 5 months ago) <Benjamin Bach>
    *   b99ca6d - Merge pull request #12 from spookylukey/fix_travis_and_tests (2 years, 5 months ago) <benjaoming>
    |\  
    | * 5636cfd - Fixed position of 'coding' lines (2 years, 5 months ago) <Luke Plant>
    | * cc262dd - Added tests for Django 1.7 (2 years, 5 months ago) <Luke Plant>
    | * c3a8f56 - Added missing migration. (2 years, 5 months ago) <Luke Plant>
    | * ea890b5 - Replaced testing on Python 3.2 with 3.3, because 3.2 is no longer supported by South (2 years, 5 months ago) <Luke Plant>
    | * f384336 - Removed some non-working test combinations. (2 years, 5 months ago) <Luke Plant>
    | * 1c60cc9 - Fixed South migrations on Django 1.4 (2 years, 5 months ago) <Luke Plant>
    | * 6a6e32f - Created tox.ini and fixed travis.yml to use tox. (2 years, 5 months ago) <Luke Plant>
    | * 5dccdcf - Fixed duplication and other issues in runtests.py (2 years, 5 months ago) <Luke Plant>
    |/  
    * aeaaed3 - fix #11 (2 years, 6 months ago) <benjaoming>
    * 7ec878a - Add docs about the south migrations module pr #9 (2 years, 6 months ago) <benjaoming>
    * b400a12 - Also related to #10 -- add same change to the migration script migrater (2 years, 6 months ago) <benjaoming>
    * e363fc3 - remove deprecation warnings, fix #10 (2 years, 6 months ago) <benjaoming>
    * 3b13838 - Pin south version and close #9 (2 years, 6 months ago) <valberg>
    *   04a135c - Merge pull request #8 from cXhristian/filter-exclude-fix (2 years, 6 months ago) <valberg>
    |\  
    | * d6ae60e - Fix filter_exclude (2 years, 6 months ago) <Christian Duvholt>
    |/  
    * 8ea5f4e - add get_or_create functionality to subscribe() function and fix tests to include subscribe() (2 years, 7 months ago) <benjaoming>
    * 18d8ae0 - (tag: alpha/0.9.4) Hopefully last remaining issue to close #6 - models __unicode__ replaced by __str__ (2 years, 7 months ago) <benjaoming>
    * 49efcf1 - add python 3 tests (2 years, 7 months ago) <benjaoming>
    * 3b08dbf - six required for travis (2 years, 7 months ago) <benjaoming>
    * 0b9b63d - add six to requirements (2 years, 7 months ago) <benjaoming>
    * 8b51161 - version bump (2 years, 7 months ago) <benjaoming>
    * d95bf4f - utility script for running tests (2 years, 7 months ago) <benjaoming>
    * 13b8c6c - (2to3) use python-modernize to have py2+3 compatibility (2 years, 7 months ago) <benjaoming>
    *   08d5836 - Merge pull request #7 from jluttine/finnish-translation (2 years, 7 months ago) <benjaoming>
    |\  
    | * 529402c - Preliminary Finnish translation (2 years, 7 months ago) <Jaakko Luttinen>
    |/  
    * 660f9c3 - add support for custom user models in south migrations #5 (2 years, 7 months ago) <benjaoming>
    *   367125b - Merge pull request #3 from destos/master (2 years, 8 months ago) <benjaoming>
    |\  
    | * d775f6e - use content_type over depreciated mimetype (2 years, 8 months ago) <Patrick Forringer>
    |/  
    *   b40ddf9 - Merge pull request #2 from holoduke/master (2 years, 9 months ago) <benjaoming>
    |\  
    | * 2be7afa - Update models.py (2 years, 9 months ago) <Gillis Haasnoot>
    |/  
    * 50af164 - goto should return to referer when url is empty string (2 years, 10 months ago) <benjaoming>
    * 60e3582 - Version bump (2 years, 10 months ago) <benjaoming>
    * 4942b2a - fix total_count going to 0 (2 years, 10 months ago) <benjaoming>
    * cf0cc32 - Return None for key type on direct notifications (2 years, 10 months ago) <benjaoming>
    * e815a58 - Fix setting user from subscription.settings (2 years, 10 months ago) <benjaoming>
    * cb721b2 - do not use simplejson (2 years, 10 months ago) <benjaoming>
    * 2940669 - str representation for Notification should use user field (2 years, 10 months ago) <benjaoming>
    * e1fad6d - make notifications without subscriptions possible in views (2 years, 10 months ago) <benjaoming>
    * 4b2cbeb - raw_id_fields for big model relations (2 years, 10 months ago) <benjaoming>
    * f56781d - (tag: alpha/0.9.2) version bump (2 years, 10 months ago) <benjaoming>
    * 08c9f8e - new subscribe() utility method (2 years, 10 months ago) <benjaoming>
    * d26f8f7 - improve database layout, add NotificationType.get_by_key (2 years, 10 months ago) <benjaoming>
    * f97b7d6 - danish translation (2 years, 10 months ago) <benjaoming>
    * 0315f6e - autopep8 (2 years, 10 months ago) <benjaoming>
    * 2b88391 - version bump + deprecate using django_nyt.notify, should be django_nyt.utils.notify (3 years ago) <benjaoming>
    * d0243f7 - 2to3 patch (3 years ago) <benjaoming>
    * e9e2254 - remove pattern causing setup.py warnings (3 years ago) <benjaoming>
    * 91f9a1b - remove old style test module (3 years ago) <benjaoming>
    * 09f0f21 - Refactor test project settings to work with newest django (and old as well) (3 years ago) <benjaoming>
    * 5df2e23 - Move old south migrations to south_migraitons module (3 years ago) <benjaoming>
    * c780cc4 - Add compat layer, move notify to utils.notify, add first test case (3 years ago) <benjaoming>
    * d4da17e - Documentation change for django_nyt.utils.notify (3 years ago) <benjaoming>
    * 9a3f383 - rename default url subtree (3 years ago) <benjaoming>
    * 641063f - pep8 setup.py + readme changes (3 years ago) <benjaoming>
    * 064a597 - badges in README (3 years, 4 months ago) <benjaoming>
    * cbc7e65 - fix django 1.6 test running (3 years, 4 months ago) <benjaoming>
    * 5a52509 - travis configuration (3 years, 4 months ago) <benjaoming>
    * e97d170 - README updates and travis hook (3 years, 4 months ago) <benjaoming>
    * f9a65a5 - README for PyPi, som PEP8 (3 years, 4 months ago) <benjaoming>
    * 94b7f1d - remove code block from index (3 years, 4 months ago) <benjaoming>
    * e2fc6cf - javascript and html example (3 years, 4 months ago) <benjaoming>
    * 4519c8c - change default url path, add more installation notes and configuration (3 years, 4 months ago) <benjaoming>
    * d20bac2 - Installation notes (3 years, 4 months ago) <benjaoming>
    * a15d990 - (tag: alpha/0.9) pypi release (3 years, 4 months ago) <benjaoming>
    * 9db86c4 - remove build directory (3 years, 4 months ago) <benjaoming>
    * 63106b0 - add new chapter, fix headlines (3 years, 4 months ago) <benjaoming>
    *   96538c7 - Merge branch 'master' of github.com:benjaoming/django-nyt (3 years, 4 months ago) <benjaoming>
    |\  
    | * c341040 - some rst formatting (3 years, 4 months ago) <benjaoming>
    * | 461ad64 - some rst formatting (3 years, 4 months ago) <benjaoming>
    |/  
    * cfb8c3d - add docs and shorten README (3 years, 4 months ago) <benjaoming>
    * 8224df0 - initial commit, moving files from django-wiki and refactoring from django_notify to django_nyt (3 years, 4 months ago) <benjaoming>
    * b7d616d - Initial commit (3 years, 4 months ago) <benjaoming>