#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask.ext.script import Manager, Shell
from flask.ext.migrate import MigrateCommand

from widelanguagedemo.app import create_app
from widelanguagedemo.settings import DevConfig, ProdConfig
from widelanguagedemo.database import db

if os.environ.get("WIDELANGUAGEDEMO_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)
TEST_CMD = "py.test tests"


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """
    return {'app': app, 'db': db}


@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main(['tests', '--verbose'])
    return exit_code

manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
