# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import admin_helpdesk
import tests


@pytest.mark.usefixtures('appi')
def test_action_start_converation():
    # user starts issue
    created = admin_helpdesk.start_conversion(tests.TESTMESSAGE)
    assert created
    tests.sleep()

    # we reply gently
    answer = admin_helpdesk.Message(
        parent=created,
        userid=tests.TESTUSER,
        text='Haben Sie nicht genug in der Portokasse?',
    )
    admin_helpdesk.write_message(answer)
    tests.sleep()

    # this user is very happy
    money = admin_helpdesk.Message(
        parent=created,
        userid=tests.TESTUSER,
        writer=tests.TESTUSER,
        text='Nein, die Box ist voll!',
    )
    admin_helpdesk.write_message(money)

    dialog = admin_helpdesk.load_messages(tests.TESTUSER, created)
    assert len(dialog) == 3
    assert dialog[0].writer  # user
    assert not dialog[1].writer  # admin
    assert dialog[2].writer  # user
