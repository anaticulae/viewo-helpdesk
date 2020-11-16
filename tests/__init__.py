#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import time

import admin_helpdesk

TESTUSER = 'abcdefghabcdefgh'
TESTMESSAGE = admin_helpdesk.Message(
    userid=TESTUSER,
    title='Problem beim Bezahlen',
    text='Ich habe Probleme beim Bezahlen!\nAchtung!\nHilfe!\nSchnell!',
    category=10,
)
NOW = 1605535477


def sleep():
    time.sleep(1)


def create_single_sample():
    # user starts issue
    created = admin_helpdesk.start_conversion(TESTMESSAGE, current=NOW)
    assert created

    # we reply gently
    answer = admin_helpdesk.Message(
        parent=created,
        userid=TESTUSER,
        text='Haben Sie nicht genug in der Portokasse?',
    )
    admin_helpdesk.write_message(answer, current=NOW + 1)

    # this user is very happy
    money = admin_helpdesk.Message(
        parent=created,
        userid=TESTUSER,
        writer=TESTUSER,
        text='Nein, die Box ist voll!',
    )
    admin_helpdesk.write_message(money, current=NOW + 2)
    return created
