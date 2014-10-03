# -*- coding: utf-8 -*-
'''Public section, including homepage and signup.'''
from flask import (Blueprint, request, render_template, flash, url_for,  # noqa
                   redirect, session)

from widelanguagedemo.utils import flash_errors  # noqa
from widelanguagedemo.database import db  # noqa

from . import forms

blueprint = Blueprint('public', __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = forms.SearchForm()
    return render_template("public/home.html", form=form)


@blueprint.route("/about/")
def about():
    return render_template("public/about.html")
