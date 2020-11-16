# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import admin_helpdesk.app


@pytest.fixture
def app(testdir):
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    appi = admin_helpdesk.app.create(
        config=dict(
            ADMIN_HELPDESK=testdir.tmpdir,
            TESTING=True,
        ))
    with appi.app_context():
        yield appi
