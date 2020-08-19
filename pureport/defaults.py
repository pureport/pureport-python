# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

"""
The Pureport defaults module holds all default values that are
used by various classes and functions..  This module provides
access to all defaults and exposes them as properties.  Some
properties can be customized with environment settings.
"""
from __future__ import absolute_import

import os
import sys

from collections import namedtuple

from pureport import transforms


ConfigItem = namedtuple('ConfigItem',
                        ('description', 'default', 'env', 'transform'))


def config_item(default, description=None, env=None, transform=None):
    transform = transform or transforms.to_str
    assert callable(transform), "transform must be a callable function"
    return ConfigItem(description, default, env, transform)


TRANSPORT_READ_TIMEOUT = config_item(
    description="HTTP socket read timeout value",
    default=10.0,
    transform=transforms.to_float,
    env="PUREPORT_TRANSPORT_READ_TIMEOUT"
)


TRANSPORT_CONNECT_TIMEOUT = config_item(
    description="HTTP connection timeout value",
    default=3.0,
    transform=transforms.to_float,
    env="PUREPORT_TRANSPORT_CONNECT_TIMEOUT"
)


CREDENTIALS_FILEPATH = config_item(
    description="Path that contains the credentials information",
    default=os.path.expanduser('~/.pureport'),
    env="PUREPORT_CREDENTIALS_FILEPATH"
)


CREDENTIALS_FILENAME = config_item(
    description="Name of the file to use for looking up credentials",
    default="credentials"
)


GENERIC_TRANSPORT_ERROR_MESSAGE = config_item(
    description="Generic error message string for pureport.transport",
    default=str(
        "unknown transport error occured, please review the caught "
        "exception for details"
    )
)


API_BASE_URL = config_item(
    description="Configures the base url to use for the Pureport API",
    default="https://api.pureport.com",
    env="PUREPORT_API_BASE_URL"
)


API_KEY = config_item(
    description="Returns the default Pureport API key",
    default=None,
    env="PUREPORT_API_KEY"
)


API_SECRET = config_item(
    description="Returns the default Pureport API secret",
    default=None,
    env="PUREPORT_API_SECRET"
)


ACCOUNT_ID = config_item(
    description="Returns the default Pureport account ID",
    default=None,
    env="PUREPORT_ACCOUNT_ID"
)


CACHE_API_SPEC = config_item(
    description="Enable or disable caching the OpenAPI spec",
    default=False,
    env="PUREPORT_CACHE_API_SPEC",
    transform=transforms.to_bool
)


WORKING_DIR = config_item(
    description="Local Pureport working directory",
    default=os.path.expanduser('~/.pureport'),
)


OPENAPI_FILE = config_item(
    description="Default path to the OpenAPI definition",
    default=os.path.expanduser('~/.pureport/openapi.json'),
    env="PUREPORT_OPENAPI_FILE"
)


LOGGING_LEVEL = config_item(
    description="Set the logging level",
    default=0,
    transform=transforms.to_int,
    env="PUREPORT_LOGGING_LEVEL"
)


AUTOMAKE_BINDINGS = config_item(
    description="Automatically run make() for API bindings",
    default=True,
    transform=transforms.to_bool,
    env="PUREPORT_AUTOMAKE_BINDINGS"
)


def defaults():
    attrs = {}
    for item in globals():
        obj = globals().get(item)
        if isinstance(obj, ConfigItem):
            name = item.lower()
            if obj.env:
                value = os.getenv(obj.env, obj.default)
            else:
                value = obj.default
            if value is not None:
                value = obj.transform(value)
            attrs[name] = value
    return namedtuple('Defaults', attrs)(**attrs)


sys.modules[__name__] = defaults()
