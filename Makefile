.PHONY all: lint build test
.PHONY lint: pylint bandit
.PHONY build: locales
.PHONY test: unittest coverage

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