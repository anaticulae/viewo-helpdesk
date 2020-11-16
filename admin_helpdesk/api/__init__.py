# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask
import utila

api_message = flask.Blueprint('api_message', __name__)  # pylint:disable=C0103

__all__ = ['api_message', 'delete', 'post', 'present']


def dump(data, name='') -> str:
    uri = flask.request.path
    name = name if name else 'data'
    data = utila.simplify(data)  # pylint:disable=E1101
    connected = {'uri': uri, name: data}
    json = flask.jsonify(connected)
    return json
