 #!/bin/env sh

pygettext3 -d messages -o locales/en_US/LC_MESSAGES/messages.pot add_source_main.py
pygettext3 -d messages -o locales/ru_RU/LC_MESSAGES/messages.pot add_source_main.py
