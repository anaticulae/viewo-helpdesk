# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import admin_helpdesk
import admin_helpdesk.message
import admin_helpdesk.message.path
import admin_helpdesk.message.serialize


def delete_message(userid: str, date: int):
    pass


def delete_history(userid: str):
    pass


def start_conversion(
        message: admin_helpdesk.message.Message,
        current: int = None,
) -> int:
    current = f'{admin_helpdesk.now()}' if current is None else f'{current}'
    outpath = os.path.join(admin_helpdesk.userpath(message.userid), current)
    # start new conversion folder
    os.makedirs(outpath, exist_ok=True)
    first_message = os.path.join(outpath, current)
    dumped = admin_helpdesk.dump_message(message)
    utila.file_create(first_message, dumped)
    return current


def write_message(message: admin_helpdesk.message.Message, current: int = None):
    current = f'{admin_helpdesk.now()}' if current is None else f'{current}'
    if message.writer is None:
        current = f'{current}!'
    dumped = admin_helpdesk.dump_message(message)
    outpath = os.path.join(
        admin_helpdesk.userpath(message.userid),
        f'{message.parent}',
        current,
    )
    utila.file_create(outpath, dumped)
