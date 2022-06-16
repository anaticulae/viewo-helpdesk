# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest

import admin_helpdesk.config
from admin_helpdesk.fixtures import appi  # pylint:disable=W0611
from admin_helpdesk.fixtures import client  # pylint:disable=W0611
from tests.fixtures import client_single  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

utilatest.setup(admin_helpdesk.config.API_PREFIX)
