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

from flask import (Blueprint, request, render_template, flash, url_for,  # noqa
                   redirect, session)

from widelanguagedemo.utils import flash_errors  # noqa
from widelanguagedemo.database import db  # noqa

from . import forms
from ..index import util

blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    is_random = False
    record = None
    record_json = None

    if request.args:
        index = util.get_index()
        lang = request.args.get('language')
        if lang == 'random':
            is_random = True
            lang = random.choice(list(index.keys()))

        records = index[lang]

        if records:
            record = random.choice(records)
            record_json = json.dumps(record, indent=2, sort_keys=True)

    if is_random:
        form = forms.SearchForm()
    else:
        form = forms.SearchForm(request.args)
    return render_template("public/home.html", form=form, record=record,
                           record_json=record_json)
