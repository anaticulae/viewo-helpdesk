# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import configos
import flask
import utilo

ADMIN_HELPDESK = 'ADMIN_HELPDESK'

ADMIN_NAME = configos.env('ADMIN_NAME', default='admin')
ADMIN_PASSWORD = configos.env('ADMIN_PASSWORD', default='secret')  # nosec

SECRET_KEY = b'helmut_max_power_abs29.nsTODOThisIsVerySecreyISwarTODO'

API_PREFIX = '/api/v0'


def helpdesk() -> str:
    path = flask.current_app.config[ADMIN_HELPDESK]
    os.makedirs(path, exist_ok=True)
    return path


def board() -> str:
    path = os.path.join(helpdesk(), 'messages')
    os.makedirs(path, exist_ok=True)
    return path


def configure(path):
    flask.current_app.config[ADMIN_HELPDESK] = path


def validate():
    try:
        _ = os.environ[ADMIN_HELPDESK]
    except KeyError:
        utilo.error(f'could not start app, define `{ADMIN_HELPDESK}`')
        sys.exit(utilo.FAILURE)
    config = {
        ADMIN_HELPDESK: os.environ[ADMIN_HELPDESK],
    }
    return config
