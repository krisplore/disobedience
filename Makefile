all: lint build test
lint: pylint
build: locales
test: unittest

pylint:
	# Lint with pylint
	pylint *.py || true

scan-translation:
	# Scan source code for gettext calls
	pygettext3 -d messages -o locales/en_US/LC_MESSAGES/messages.pot add_source_main.py
	pygettext3 -d messages -o locales/ru_RU/LC_MESSAGES/messages.pot add_source_main.py

locales: locales/en_US/LC_MESSAGES/messages.mo locales/ru_RU/LC_MESSAGES/messages.mo

locales/en_US/LC_MESSAGES/messages.mo: locales/en_US/LC_MESSAGES/messages.pot
	# Compiling translation
	msgfmt -v -o $@ $<

locales/ru_RU/LC_MESSAGES/messages.mo: locales/ru_RU/LC_MESSAGES/messages.pot
	# Compiling ru translation
	msgfmt -v -o $@ $<

unittest:
	./venv/bin/python -m unittest discover tests/

setup:
	python -m venv venv

install-deps:
	./venv/bin/pip install -r requirements.txt

collect-deps:
	./venv/bin/pip freeze > requirements.txt