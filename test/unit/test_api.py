# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import os
import re

from pureport import api


def test_api_methods_exist():
    basepath = os.path.dirname(__file__)
    content = open(os.path.join(basepath, '../openapi.json')).read()
    methods = re.findall('operationId: (.+)', content, re.M)
    assert set(methods).issubset(dir(api))
