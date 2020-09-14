# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import pytest
from pureport import models
from .test_helpers import ModelData
models.make()


@pytest.mark.parametrize(
    "modela",
    [
        ModelData("Network", type="Network", name="", remove=True),
        ModelData("Connection", type="AWS_DIRECT_CONNECT", name="", remove=True),
        ModelData("Connection", type="AWS_DIRECT_CONNECT", speed="", remove=True),
        ModelData(
            "Connection", type="AWS_DIRECT_CONNECT", billing_term="HOURLY", remove=True
        ),
        ModelData(
            "Connection",
            type="AWS_DIRECT_CONNECT",
            high_availability="HOURLY",
            remove=True,
        ),
        ModelData("Connection", type="AWS_DIRECT_CONNECT", location="", remove=True),
    ],
)
def test_model_load_exception(modela):
    with pytest.raises(TypeError):
        result = models.load(modela.type, modela.data)
