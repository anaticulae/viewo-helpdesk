# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import tests


def test_have_conversation(client):
    tests.login(client)
    with tests.session(client):
        result = tests.send_message(
            client,
            userid=tests.TESTUSER,
            title='Ich habe eine Frage',
            text='Langtext',
        )
        parent = result['success']['date']
    with tests.session_admin(client):
        result = tests.send_message(
            client,
            userid=tests.TESTUSER,
            text=('Ein Techniker ist informiert und wir sich um Ihr '
                  'Problem kümmern - bleiben Sie auf Empfang.'),
            parent=parent,
        )
    tests.sleep()

    with tests.session(client):
        tests.send_message(
            client,
            userid=tests.TESTUSER,
            text='Haben Sie vielen Dank!',
            parent=parent,
        )
        dialog = utilatest.apicall(client, f'/dialog/{tests.TESTUSER}/{parent}')
    assert len(dialog['messages']) == 3

    with tests.session_admin(client):
        userdialogs = utilatest.apicall(client, f'/dialogs/{tests.TESTUSER}')
    assert len(userdialogs['dialogs']) == 1
