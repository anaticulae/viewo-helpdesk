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


def sleep():
    time.sleep(1)
