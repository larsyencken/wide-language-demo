# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
import pytest
from flask import url_for


class TestLanguageSearch:
    def test_homepage_returns_200(self, testapp):
        res = testapp.get("/")
        assert res.status_code == 200

    def test_search_for_included_sample_yields_result(self, testapp):
        res = testapp.get("/")
        form = res.forms['search-form']
        form['language'] = 'cmn'  # Mandarin Chinese

        res = form.submit()
        assert res.status_code == 200
        assert '<audio' in res

    def test_search_for_bad_language_name_yields_error(self, testapp):
        res = testapp.get("/")
        form = res.forms['search-form']
        form['language'] = 'English'  # not an ISO 693-3 code

        res = form.submit()
        assert res.status_code == 200
        assert 'ISO 693-3 language code' in res


    def test_search_for_missing_sample_yields_error(self, testapp):
        res = testapp.get("/")
        form = res.forms['search-form']
        form['language'] = 'lit'  # Mandarin Chinese

        res = form.submit()
        assert res.status_code == 200
        assert '<audio' not in res
        assert 'not a known language' not in res
        assert 'no samples of this language' in res
