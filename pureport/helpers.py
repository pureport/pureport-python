# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

"""
This module provides a set of helper functions that can be used to perform
various activties.

"""
from __future__ import absolute_import

import os
import json
import logging

from functools import lru_cache

from pureport import defaults


log = logging.getLogger(__name__)


def print_response(response):
    """Pretty prints a response object to stdout

    :param response: a HTTP response object
    :type response: :class:`pureport.transport.Response`
    """
    assert hasattr(response, 'json'), "missing required attribute `json`"
    if response.json:
        print(json.dumps(response.json, indent=4, sort_keys=True))


def print_json(obj):
    """Pretty prints a Python dict to stdout as JSON

    :param content: any Python dict object
    :type content: dict
    """
    assert isinstance(obj, (list, dict)), "invalid type for obj"
    print(json.dumps(obj, indent=4, sort_keys=True))


def first(val):
    """Returns the first element of a list-type object

    :param val: sequence of elements
    :type val: object

    :returns: first element
    :rtype: object
    """
    if val and isinstance(val, (list, tuple, set)):
        val = val[0]
    return val


@lru_cache(maxsize=16)
def get_api(session):
    if os.path.exists(defaults.openapi_file):
        log.debug("loading openapi spec from file {}".format(defaults.openapi_file))
        api_spec = json.loads(open(defaults.openapi_file).read())
    elif os.path.exists(os.path.join(os.path.dirname(__file__), 'openapi.json')):
        log.debug("loading openapi spec from embedded")
        api_spec = json.loads(open(os.path.join(os.path.dirname(__file__), 'openapi.json')).read())
    else:
        log.debug("retrieving openapi spec from remote server")
        api_spec = session.get('/openapi.json')
        if defaults.cache_api_spec is True:
            with open(defaults.openapi_file, 'w') as f:
                f.write(json.dumps(api_spec))
    return api_spec


def get_value(path, obj):
    """Returns the value of key in a nested data structure

    :param path: The path to the value to be returned
    :type path: str

    :param obj: Source of the data to return a value from
    :type obj: obj

    :return: Value based on the path or None
    :rtype: object
    """
    try:
        path = path.split('.')
        for item in path:
            try:
                item = int(item)
            except ValueError:
                pass
            obj = obj[item]
        return obj
    except KeyError:
        return None
