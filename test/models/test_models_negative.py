# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import pytest
from pureport import api
from .test_helpers import ModelData


@pytest.mark.parametrize(
    "model",
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
        ModelData("Connection", type="AWS_DIRECT_CONNECT", speed=150),
        ModelData("Connection", type="AWS_DIRECT_CONNECT", billing_term="None"),
    ],
)
def test_model_load_exception(model):
    with pytest.raises(TypeError):
        result = api.models.load(model.type, model.data)
