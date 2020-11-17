# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import admin_helpdesk.app

CONFIG = {'ADMIN_HELPDESK': os.environ['ADMIN_HELPDESK']}

instance = admin_helpdesk.app.create(CONFIG)  # pylint:disable=C0103
