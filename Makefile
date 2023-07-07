all: lint build test
lint: pylint
build: locales
test: unittest

pylint:
	# Lint with pylint
	pylint --recursive=y intel || true

scan-translation:
	# Scan source code for gettext calls
	pygettext3 -d disobedience -o locales/en_US/LC_MESSAGES/disobedience.pot intel/source/add.py
	pygettext3 -d disobedience -o locales/ru_RU/LC_MESSAGES/disobedience.pot intel/source/add.py

locales: locales/en_US/LC_MESSAGES/disobedience.mo locales/ru_RU/LC_MESSAGES/disobedience.mo

locales/en_US/LC_MESSAGES/disobedience.mo: locales/en_US/LC_MESSAGES/disobedience.pot
	# Compiling translation
	msgfmt --check --strict -v -o $@ $<

locales/ru_RU/LC_MESSAGES/disobedience.mo: locales/ru_RU/LC_MESSAGES/disobedience.pot
	# Compiling ru translation
	msgfmt --check --strict -v -o $@ $<

unittest:
	./venv/bin/python -m unittest discover tests/

setup:
	python -m venv venv

install-deps:
	./venv/bin/pip install -r requirements.txt

collect-deps:
	./venv/bin/pip freeze > requirements.txt