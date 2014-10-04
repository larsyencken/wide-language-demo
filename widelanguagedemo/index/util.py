# -*- coding: utf-8 -*-
#
#  util.py
#  wide-language-demo
#

"""
Read the wide-language-index dataset.
"""

import glob
from os import path
from collections import defaultdict
import json


_CACHE = {}


def get_index():
    return _lazy_fetch('index', build_index)


def get_languages():
    return _lazy_fetch('languages', build_languages)


def _lazy_fetch(var_name, factory):
    global _CACHE

    if var_name not in _CACHE:
        _CACHE[var_name] = factory()

    return _CACHE[var_name]


def build_index():
    index = defaultdict(list)
    pattern = path.join(path.dirname(__file__), 'data/index/*/*.json')
    for f in glob.glob(pattern):
        rec = json.load(open(f))
        index[rec['language']].append(rec)

    return index


def build_languages():
    codes = set()
    languages = []
    input_file = path.join(path.dirname(__file__),
                           'data/ext/name_index_20140320.json')
    records = json.load(open(input_file))
    for rec in records:
        inverted_name = rec['inverted_name']
        code = rec['id']
        codes.add(code)
        languages.append('{0} [{1}]'.format(inverted_name, code))

    languages.sort()

    return {'codes': codes,
            'languages': languages}
