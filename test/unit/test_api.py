# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import os
import re

from unittest.mock import patch

from pureport import api


@patch.object(api, 'Session')
def test_api_methods_exist(mock_session):
    basepath = os.path.dirname(__file__)
    content = open(os.path.join(basepath, '../openapi.json')).read()
    mock_session.get.return_value = content

    methods = re.findall('operationId: (.+)', content, re.M)
    assert set(methods).issubset(dir(api))
