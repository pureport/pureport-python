# -*- coding: utf-8 -*_
#
# Copyright (c) 2020, Pureport, Inc.
# All Rights Reserved

import pytest
import random
from pureport import models
from ..utils import utils
from .test_helpers import ModelData
models.make()


@pytest.mark.parametrize(
    "model",
    [
        ModelData("Network"),
        ModelData("Connection", type="AWS_DIRECT_CONNECT"),
        ModelData("Connection", type="AZURE_EXPRESS_ROUTE"),
        ModelData("Connection", type="GOOGLE_CLOUD_INTERCONNECT"),
        ModelData("Connection", type="SITE_IPSEC_VPN"),
        ModelData(
            "Connection",
            type="AWS_DIRECT_CONNECT",
            description=utils.random_string(min=1, max=1024),
        ),
        ModelData(
            "Connection",
            type="AWS_DIRECT_CONNECT",
            customer_networks=[{"name": "Net1", "address": "10.0.0.1/24"}],
        ),
        ModelData(
            "Connection",
            type="AWS_DIRECT_CONNECT",
            advertise_internal_routes=random.choice([True, False]),
        ),
    ],
)
def test_model_load(model):
    assert models.load(model.type, model.data)
