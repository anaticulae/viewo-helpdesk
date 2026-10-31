# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import admin_helpdesk.app
import admin_helpdesk.config

CONFIG = {
    admin_helpdesk.config.VIEWO_HELPDESK:
        os.environ[admin_helpdesk.config.VIEWO_HELPDESK]
}

instance = admin_helpdesk.app.create(CONFIG)  # pylint:disable=C0103
