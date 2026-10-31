# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo

import admin_helpdesk
import admin_helpdesk.message
import admin_helpdesk.message.path
import admin_helpdesk.message.serialize


def delete_message(userid: str, date: int):  # pylint:disable=W0613
    pass


def delete_history(userid: str):  # pylint:disable=W0613
    pass


def start_conversion(
    message: admin_helpdesk.message.Message,
    current: int = None,
) -> int:
    current = f'{utilo.now()}' if current is None else f'{current}'
    outpath = os.path.join(admin_helpdesk.userpath(message.userid), current)
    # start new conversion folder
    os.makedirs(outpath, exist_ok=True)
    first_message = os.path.join(outpath, current)
    dumped = admin_helpdesk.dump_message(message)
    utilo.file_create(first_message, dumped)
    return current


def write_message(message: admin_helpdesk.message.Message, current: int = None):
    current = f'{utilo.now()}' if current is None else f'{current}'
    if message.writer is None:
        current = f'{current}!'
    dumped = admin_helpdesk.dump_message(message)
    outpath = os.path.join(
        admin_helpdesk.userpath(message.userid),
        f'{message.parent}',
        current,
    )
    utilo.file_create(outpath, dumped)
