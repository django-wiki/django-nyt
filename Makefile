.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	pep8 django_nyt

test:
	./runtests.py

test-all:
	tox

coverage:
	coverage run --source django_nyt runtests.py
	coverage report -m

docs:
	rm -f docs/modules.rst
	rm -f docs/django_nyt*.rst
	$(MAKE) -C docs clean
	sphinx-apidoc -d 10 -H "Python Reference" -o docs/ django_nyt django_nyt/tests django_nyt/migrations
	$(MAKE) -C docs html
	# sphinx-build -b linkcheck ./docs docs/_build/
	sphinx-build -b html ./docs docs/_build/

release: clean sdist
	echo "Packing source dist..."
	twine upload -s dist/*

sdist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
