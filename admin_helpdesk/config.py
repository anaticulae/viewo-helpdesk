# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask

ADMIN_HELPDESK = 'ADMIN_HELPDESK'

SECRET_KEY = b'helmut_max_power_abs29.nsTODOThisIsVerySecreyISwarTODO'


def helpdesk() -> str:
    path = flask.current_app.config[ADMIN_HELPDESK]
    os.makedirs(path, exist_ok=True)
    return path


def board() -> str:
    path = os.path.join(helpdesk(), 'messages')
    os.makedirs(path, exist_ok=True)
    return path
