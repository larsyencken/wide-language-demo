# -*- coding: utf-8 -*-
#
#  views.py
#  wide-language-demo
#

import json

import flask

blueprint = flask.Blueprint('index', __name__, static_folder="../static")

from . import util


@blueprint.route("/languages.json", methods=["GET"])
def languages():
    return flask.Response(json.dumps(util.get_languages()['languages']),
                          mimetype='application/json')
