# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import http

import utilatest

import admin_helpdesk.api.auth
import tests


def test_dialog_list_admin(client_single):
    tests.login_admin(client_single)
    dialogs = utilatest.apicall(client_single, '/dialogs')
    assert dialogs['dialogs'][0]['userid'] == tests.TESTUSER


def test_dialog_list_user(client_single):
    tests.login(client_single)
    dialogs = utilatest.apicall(
        client_single,
        '/dialogs',
        expected=http.HTTPStatus.UNAUTHORIZED,
    )
    assert dialogs == admin_helpdesk.api.auth.NO_ACCESS
