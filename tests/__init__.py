#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import contextlib
import time

import utilotest

import viewo_helpdesk
import viewo_helpdesk.config

TESTUSER = 'abcdefghabcdefgh'
TESTPASSWORD = '88888891'
TESTMESSAGE = viewo_helpdesk.Message(
    userid=TESTUSER,
    title='Problem beim Bezahlen',
    text='Ich habe Probleme beim Bezahlen!\nAchtung!\nHilfe!\nSchnell!',
    category=10,
)
NOW = 1605535477
TESTDATE = NOW


def sleep():
    time.sleep(1)


def login(client, userid=TESTUSER, password=TESTPASSWORD):
    result = utilotest.apipost(
        client,
        '/auth',
        {
            'user': userid,
            'password': password,
        },
    )
    assert 'DONE' in result or 'link' in str(result)


def logout(client):
    result = utilotest.apicall(client, '/logout')
    assert 'DONE' in result


def login_admin(client):
    login(
        client,
        userid=viewo_helpdesk.config.ADMIN_NAME,
        password=viewo_helpdesk.config.ADMIN_PASSWORD,
    )


@contextlib.contextmanager
def session(client):
    login(client)
    yield
    logout(client)


@contextlib.contextmanager
def session_admin(client):
    login_admin(client)
    yield
    logout(client)


def send_message(client, userid, text, title=None, parent=None, category=10):
    data = {
        'userid': userid,
        'title': title,
        'text': text,
        'parent': parent,
        'category': category,
    }
    result = utilotest.apipost(client, '/dialog/add', data)
    return result


def create_single_sample():
    # user starts issue
    created = viewo_helpdesk.start_conversion(TESTMESSAGE, current=NOW)
    assert created

    # we reply gently
    answer = viewo_helpdesk.Message(
        parent=created,
        userid=TESTUSER,
        text='Haben Sie nicht genug in der Portokasse?',
    )
    viewo_helpdesk.write_message(answer, current=NOW + 1)

    # this user is very happy
    money = viewo_helpdesk.Message(
        parent=created,
        userid=TESTUSER,
        writer=TESTUSER,
        text='Nein, die Box ist voll!',
    )
    viewo_helpdesk.write_message(money, current=NOW + 2)
    return created
