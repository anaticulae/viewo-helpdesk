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


def load_messages(userid: str, date: int) -> 'admin_helpdesk.Messages':
    date = f'{date}'
    board = admin_helpdesk.board()
    path = os.path.join(board, userid, date)
    dates = utila.file_list(path)
    # remove admin mark to clarify date
    dates = [item.replace('!', '') for item in dates]
    loaded = [load_message(userid, date, msgdate) for msgdate in dates]
    return loaded


def load_message(
        userid: str,
        start: int,
        date: str = None,
) -> 'admin_helpdesk.Message':
    # load header if no date is given
    date = date if date else start
    start, date = f'{start}', f'{date}'
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


def load_dialogs(user: str = None) -> 'admin_helpdesk.Dialogs':
    board = admin_helpdesk.board()
    result = []
    users = utila.directory_list(board) if user is None else [user]  # pylint:disable=E1101
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


def valid_user(userid: str) -> bool:
    board = admin_helpdesk.board()
    userpath = os.path.join(board, userid)
    if not os.path.exists(userpath):
        return False
    return True


def valid_dialog(userid: str, date: int) -> bool:
    if not valid_user(userid):
        return False
    date = f'{date}'
    board = admin_helpdesk.board()
    dialogpath = os.path.join(board, userid, date)
    if not os.path.exists(dialogpath):
        return False
    return True


def load_after(date: int, userid: int = None):
    pass


def load_before(data: int, userid: int = None):
    pass
