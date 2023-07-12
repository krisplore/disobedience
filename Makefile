all: lint build test
lint: pylint bandit
build: locales
test: unittest coverage

pylint:
	# Lint with pylint
	PYTHONPATH=$(shell pwd) venv/bin/pylint --recursive=y src tests || true

bandit:
	venv/bin/bandit -r src tests

scan-translation:
	# Scan source code for gettext calls
	pygettext3 -d disobedience -o locales/en_US/LC_MESSAGES/disobedience.pot src/add.py
	pygettext3 -d disobedience -o locales/ru_RU/LC_MESSAGES/disobedience.pot src/add.py

locales: locales/en_US/LC_MESSAGES/disobedience.mo locales/ru_RU/LC_MESSAGES/disobedience.mo

locales/en_US/LC_MESSAGES/disobedience.mo: locales/en_US/LC_MESSAGES/disobedience.pot
	# Compiling translation
	msgfmt --check --strict -v -o $@ $<

locales/ru_RU/LC_MESSAGES/disobedience.mo: locales/ru_RU/LC_MESSAGES/disobedience.pot
	# Compiling ru translation
	msgfmt --check --strict -v -o $@ $<

unittest:
	venv/bin/coverage run -m unittest discover tests/

coverage:
	venv/bin/coverage report

setup:
	python -m venv venv

install-deps:
	venv/bin/pip install -r requirements.txt

collect-deps:
	venv/bin/pip freeze > requirements.txt