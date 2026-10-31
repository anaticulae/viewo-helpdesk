# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import utilotest

import tests
import viewo_helpdesk.api.auth


def test_dialog_list_admin(client_single):
    tests.login_admin(client_single)
    dialogs = utilotest.apicall(client_single, '/dialogs')
    assert dialogs['dialogs'][0]['userid'] == tests.TESTUSER


def test_dialog_list_user(client_single):
    tests.login(client_single)
    dialogs = utilotest.apicall(
        client_single,
        '/dialogs',
        expected=http.HTTPStatus.UNAUTHORIZED,
    )
    assert dialogs == viewo_helpdesk.api.auth.NO_ACCESS
