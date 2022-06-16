# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import tests


def test_message_present(client_single):
    tests.login(client_single)
    messages = utilatest.apicall(
        client_single,
        f'/dialog/{tests.TESTUSER}/{tests.TESTDATE}',
    )
    assert len(messages['messages']) == 3
