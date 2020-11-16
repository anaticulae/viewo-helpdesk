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
import admin_helpdesk.config


def load_messages(userid: str, date: int) -> admin_helpdesk.Messages:
    board = admin_helpdesk.board()
    path = os.path.join(board, userid, date)
    dates = utila.file_list(path)
    # remove admin mark to clarify date
    dates = [item.replace('!', '') for item in dates]
    loaded = [load_message(userid, date, msgdate) for msgdate in dates]
    return loaded


def load_message(userid: str, start: int, date: str) -> admin_helpdesk.Message:
    board = admin_helpdesk.board()
    message = admin_helpdesk.Message(
        userid=userid,
        parent=start,
        date=int(date),
    )
    path = os.path.join(board, userid, start)
    if os.path.exists(os.path.join(path, date)):
        # user message
        path = os.path.join(path, date)
        message.writer = userid
    else:
        # admin message
        path = os.path.join(path, f'{date}!')
    message_raw = utila.file_read(path)
    title, text = message_raw.split('\n\n', maxsplit=1)
    if title != 'None':
        message.title = title
    message.text = text
    return message


def load_dialogs() -> admin_helpdesk.Dialogs:
    board = admin_helpdesk.board()
    result = []
    users = utila.directory_list(board)  # pylint:disable=E1101
    for userid in users:
        dialogs = utila.directory_list(os.path.join(board, userid))  # pylint:disable=E1101
        for dialog in dialogs:
            dialog = int(dialog)
            result.append(admin_helpdesk.Dialog(userid=userid, date=dialog))
    return result


def load_users() -> list:
    board = admin_helpdesk.board()
    users = utila.file_list(board)
    return users


def load_after(date: int, userid: int = None):
    pass


def load_before(data: int, userid: int = None):
    pass
