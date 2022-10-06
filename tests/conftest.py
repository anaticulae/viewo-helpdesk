# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# pylint:disable=W0611
import utilatest
from utilatest import mp
from utilatest import td

import admin_helpdesk.config
from admin_helpdesk.fixtures import appi
from admin_helpdesk.fixtures import client
from tests.fixtures import client_single

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

utilatest.setup(admin_helpdesk.config.API_PREFIX)
