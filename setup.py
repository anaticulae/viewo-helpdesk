#!/usr/bin/env python
# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

PACKAGES = [
    'admin_helpdesk',
    'admin_helpdesk.api',
    'admin_helpdesk.message',
    'admin_helpdesk.view',
]
ENTRY_POINTS = dict(console_scripts=[
    'admin_helpdesk = admin_helpdesk.cli:main',
])

if __name__ == "__main__":
    utila.install(
        __file__,
        include_package_data=True,
    )
