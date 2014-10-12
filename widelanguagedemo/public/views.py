# -*- coding: utf-8 -*-
#
#  views.py
#  wide-language-index-demo
#

"""
Public facing frontpage.
"""

import json
import random

from flask import (Blueprint, request, render_template, redirect)

from . import forms
from ..index import util

blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    language = request.args.get('language')
    if language is not None and not language:
        return redirect('/')

    elif language:
        return _render_language(language)

    form = forms.SearchForm()
    return render_template("public/home.html",
                           form=form,
                           has_query=False)


def _render_language(language):
    index = util.get_index()
    if language == 'random':
        language = random.choice(list(index.keys()))
        return redirect('/?language={0}'.format(language))

    records = index.get(language)
    inverted_name = util.get_languages().get(language)

    record = None
    record_json = None
    if records:
        record = random.choice(records)
        record_json = json.dumps(record, indent=2, sort_keys=True)

    form = forms.SearchForm(request.args)
    return render_template("public/home.html", form=form, record=record,
                           record_json=record_json,
                           inverted_name=inverted_name,
                           has_query=bool(request.args),
                           is_valid=bool(inverted_name is not None))
