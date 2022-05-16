# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools
import http

import flask
import flask_login
import utila

import admin_helpdesk
import admin_helpdesk.config

api_auth = flask.Blueprint('api_auth', __name__)  # pylint:disable=C0103
api_message = flask.Blueprint('api_message', __name__)  # pylint:disable=C0103

__all__ = ['api_auth', 'api_message', 'auth', 'delete', 'post', 'present']


def dump(data, name='', uri='') -> str:
    uri = uri if uri else flask.request.path
    name = name if name else 'data'
    data = utila.simplify(data)  # pylint:disable=E1101
    connected = {'uri': uri, name: data}
    json = flask.jsonify(connected)
    return json


def success(message: str = 'completed', **args):
    result = flask.jsonify({
        'message': message,
        **args,
    })
    return result, http.HTTPStatus.OK


def notfound(message: str):
    result = flask.jsonify({
        'error': 'not found',
        'message': message,
    })
    return result, http.HTTPStatus.NOT_FOUND


def bad(message: str):
    result = flask.jsonify({
        'error': 'bad request',
        'message': message,
    })
    return result, http.HTTPStatus.BAD_REQUEST


def internal(message: str):
    result = flask.jsonify({
        'error': 'internal',
        'message': message,
    })
    return result, http.HTTPStatus.INTERNAL_SERVER_ERROR


def api_call(path):
    return admin_helpdesk.config.API_PREFIX + path


def valid_user(function):

    @functools.wraps(function)
    def decorated_function(*args, **kwargs):
        userid = kwargs['userid']
        currentuser = flask_login.current_user
        if not currentuser.is_authenticated:
            return bad('login required')
        if not userid and not currentuser.is_admin:
            return notfound('not accessable')
        if userid and not currentuser.is_admin:
            if not admin_helpdesk.valid_user(userid):
                return notfound(f'could not locate `{userid}`')
            if currentuser.get_id() != userid:
                return notfound('not accessable')
        return function(*args, **kwargs)

    return decorated_function


def valid_dialog(function):

    @functools.wraps(function)
    def decorated_function(*args, **kwargs):
        userid = kwargs['userid']
        date = kwargs['date']
        if not admin_helpdesk.valid_dialog(userid, date):
            return notfound(f'could not locate `{userid}` `{date}`')
        return function(*args, **kwargs)

    return decorated_function
