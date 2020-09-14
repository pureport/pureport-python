# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import pytest
from pureport import models
from .test_helpers import ModelData
models.make()


@pytest.mark.parametrize(
    "model",
    [
        ModelData("Connection", type="AWS_DIRECT_CONNECT", speed=150),
        ModelData("Connection", type="AWS_DIRECT_CONNECT", billing_term="None"),
        ModelData(
            "Connection",
            type="AWS_DIRECT_CONNECT",
            customer_networks=[{"name": 100, "address": 100}]
        )
    ],
)
def test_model_load_exception(model):
    with pytest.raises(ValueError):
        result = models.load(model.type, model.data)
