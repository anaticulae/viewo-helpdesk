# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import tests
from admin_helpdesk import client  # pylint:disable=W0611


@pytest.fixture
def client_single(client):  # pylint:disable=W0621
    tests.create_single_sample()
    return client
