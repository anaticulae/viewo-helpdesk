# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import tests


def test_have_conversation(client):
    tests.login(client)
    result = tests.send_message(
        client,
        userid=tests.TESTUSER,
        title='Ich habe eine Frage',
        text='Langtext',
    )
    parent = result['success']['date']
    tests.logout(client)
    tests.login_admin(client)
    result = tests.send_message(
        client,
        userid=tests.TESTUSER,
        text=('Ein Techniker ist informiert und wir sich um Ihr '
              'Problem kümmern - bleiben Sie auf Empfang.'),
        parent=parent,
    )
    tests.logout(client)
    tests.sleep()
    tests.login(client)
    tests.send_message(
        client,
        userid=tests.TESTUSER,
        text='Haben Sie vielen Dank!',
        parent=parent,
    )

    dialog = utilatest.apicall(client, f'/dialog/{tests.TESTUSER}/{parent}')
    assert len(dialog['messages']) == 3

    tests.logout(client)
    tests.login_admin(client)
    userdialogs = utilatest.apicall(client, f'/dialogs/{tests.TESTUSER}')
    assert len(userdialogs['dialogs']) == 1
