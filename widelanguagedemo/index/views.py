# -*- coding: utf-8 -*-
#
#  views.py
#  wide-language-demo
#

import flask

blueprint = flask.Blueprint('index', __name__, static_folder="../static")
