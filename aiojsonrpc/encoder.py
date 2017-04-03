#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the `aiojsonrpc` package.
# (c) 2016-2017 Kozlovski Lab <welcome@kozlovskilab.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
"""
:Authors:
    - `Vladimir Kozlovski <vladimir@kozlovskilab.com>`_
"""
from json import JSONEncoder
from datetime import datetime


class BaseEncoder(JSONEncoder):
    """
    A C{json.JSONEncoder} subclass to encode documents that have fields of
    type C{bson.objectid.ObjectId}, C{datetime.datetime}
    """
    def default(self, obj, **kwargs):
        if isinstance(obj, datetime):
            return obj.strftime('%a, %d %b %Y %H:%M:%S GMT')
        else:
            return JSONEncoder.default(self, obj, **kwargs)
