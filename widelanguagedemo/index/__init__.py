# -*- coding: utf-8 -*-
#
#  __init__.py
#  wide-language-index-demo
#

"""
The actual JSON records of the index dataset, loaded lazily.
"""

import json
from os import path
import glob
from collections import defaultdict


_INDEX = None


def get_index():
    global _INDEX

    if _INDEX is not None:
        return _INDEX

    index = defaultdict(list)
    pattern = path.join(path.dirname(__file__), 'data/index/*/*.json')
    for f in glob.glob(pattern):
        rec = json.load(open(f))
        index[rec['language']].append(rec)

    _INDEX = index

    return index
