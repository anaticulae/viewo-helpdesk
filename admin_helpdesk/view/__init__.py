# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

view_admin = flask.Blueprint('view_admin', __name__)  # pylint:disable=C0103
view_login = flask.Blueprint('view_login', __name__)  # pylint:disable=C0103
view_user = flask.Blueprint('view_user', __name__)  # pylint:disable=C0103

__all__ = ['admin', 'login', 'user', 'view_admin', 'view_login', 'view_user']
