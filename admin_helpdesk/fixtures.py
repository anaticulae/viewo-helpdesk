# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import admin_helpdesk.api.auth
import admin_helpdesk.app


@pytest.fixture
def appi(td):
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    created = admin_helpdesk.app.create(config=dict(
        ADMIN_HELPDESK=td.tmpdir,
        TESTING=True,
    ))
    with created.app_context():
        yield created


@pytest.fixture
def client(appi, mp):  # pylint:disable=W0621
    """A test client for the app."""
    with mp.context() as context:

        def verify_password(user: str, password: str) -> bool:  # pylint:disable=W0613
            return True

        context.setattr(
            admin_helpdesk.api.auth,
            'verify_password',
            verify_password,
        )
        yield appi.test_client()
