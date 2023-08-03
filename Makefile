.PHONY all: lint build test
.PHONY lint: pylint bandit
.PHONY build: locales
.PHONY test: smoke-test unittest coverage

.PHONY pylint:
	# Lint with pylint
	PYTHONPATH=$(shell pwd) venv/bin/pylint --recursive=y intel tests || true

bandit:
	venv/bin/bandit -r intel tests

scan-translation:
	# Scan source code for gettext calls
	pygettext3 -d disobedience -o locales/en_US/LC_MESSAGES/disobedience.pot intel/source/add.py
	pygettext3 -d disobedience -o locales/en_US/LC_MESSAGES/disobedience.pot intel/main.py
	pygettext3 -d disobedience -o locales/ru_RU/LC_MESSAGES/disobedience.pot intel/source/add.py

.PHONY locales: locales/en_US/LC_MESSAGES/disobedience.mo locales/ru_RU/LC_MESSAGES/disobedience.mo

locales/en_US/LC_MESSAGES/disobedience.mo: locales/en_US/LC_MESSAGES/disobedience.pot
	# Compiling translation
	msgfmt --check --strict -v -o $@ $<

locales/ru_RU/LC_MESSAGES/disobedience.mo: locales/ru_RU/LC_MESSAGES/disobedience.pot
	# Compiling ru translation
	msgfmt --check --strict -v -o $@ $<

smoke-test:
	intel/main.py source add opt -c Jack -i '36UKB2D, 9PH3XW4'
	intel/main.py source edit --where.id ac03eeee-b7df-451d-8bda-12ab2f1f6a21 --new.tags 'X, Y, Z'

unittest:
	venv/bin/coverage run -m unittest discover tests/

coverage:
	venv/bin/coverage html --directory=reports/coverage

setup:
	python -m venv venv

install-deps:
	venv/bin/pip install -r requirements.txt

collect-deps:
	venv/bin/pip freeze > requirements.txt

clean:
	rm locales/en_US/LC_MESSAGES/disobedience.mo
	rm locales/ru_RU/LC_MESSAGES/disobedience.mo

.PHONY: all lint build test pylint bandit scan-translation locales unittest coverage setup install-deps collect-deps clean