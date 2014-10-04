#
#  Makefile
#

ENV = /tmp/virtualenv/widelanguagedemo
RUN = $(ENV)/bin/python manage.py
LINT = $(ENV)/bin/flake8

.PHONY: help env test lint dbmigrate dbupgrade serve

help:
	@echo "Available admin commands:"
	@echo ""
	@echo "make env         setup a virtualenv environment"
	@echo "make test        run unit tests"
	@echo "make lint        lint all source code"
	@echo "make dbmigrate   generate a new migration"
	@echo "make dbupgrade   apply any pending migrations"
	@echo "make dbshell     enter a database shell"
	@echo "make serve       run the debug server"
	@echo "make prodserve   run the production server"
	@echo ""

env:
	mkdir -p $$(dirname $(ENV))
	test -d $(ENV) || virtualenv $(ENV)
	$(ENV)/bin/pip install -r requirements/dev.txt

test:
	$(RUN) test

lint:
	find . -name '*.py' | xargs $(LINT)

dbmigrate:
	$(RUN) db migrate

dbupgrade:
	$(RUN) db upgrade

dbshell:
	$(RUN) db shell

serve:
	$(RUN) runserver

prodserve:
	WIDELANGUAGEDEMO_ENV=prod $(ENV)/bin/gunicorn widelanguagedemo.app:create_app\(\) -b 0.0.0.0:5000 -w 3
