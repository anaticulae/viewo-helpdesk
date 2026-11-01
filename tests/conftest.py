# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# pylint:disable=W0611
import utilotest
from utilotest import mp
from utilotest import td

import viewo_helpdesk.config
from tests.fixtures import client_single
from viewo_helpdesk.fixtures import appi
from viewo_helpdesk.fixtures import client

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

utilotest.setup(viewo_helpdesk.config.API_PREFIX)
