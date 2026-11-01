# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import tests
import viewo_helpdesk


@pytest.mark.usefixtures('appi')
def test_action_start_converation():
    # user starts issue
    created = tests.create_single_sample()

    dialog = viewo_helpdesk.load_messages(tests.TESTUSER, created)
    assert len(dialog) == 3
    assert dialog[0].writer  # user
    assert not dialog[1].writer  # admin
    assert dialog[2].writer  # user
