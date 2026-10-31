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

import viewo_helpdesk
import viewo_helpdesk.config


def load_messages(userid: str, date: int) -> 'viewo_helpdesk.Messages':
    date = f'{date}'
    board = viewo_helpdesk.board()
    path = os.path.join(board, userid, date)
    dates = utilo.file_list(path)
    # remove admin mark to clarify date
    dates = [item.replace('!', '') for item in dates]
    loaded = [load_message(userid, date, msgdate) for msgdate in dates]
    # sort by date
    loaded.sort(key=lambda x: x.date)
    return loaded


def load_message(
    userid: str,
    start: int,
    date: str = None,
) -> 'viewo_helpdesk.Message':
    # load header if no date is given
    date = date if date else start
    start, date = f'{start}', f'{date}'
    board = viewo_helpdesk.board()
    message = viewo_helpdesk.Message(
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
    message_raw = utilo.file_read(path)
    title, text = message_raw.split('\n\n', maxsplit=1)
    if title != 'None':
        message.title = title
    message.text = text
    return message


def load_dialogs(user: str = None) -> 'viewo_helpdesk.Dialogs':
    board = viewo_helpdesk.board()
    result = []
    users = utilo.directory_list(board) if user is None else [user]  # pylint:disable=E1101
    for userid in users:
        dialogs = utilo.directory_list(os.path.join(board, userid))  # pylint:disable=E1101
        for dialog in dialogs:
            dialog = int(dialog)
            title = load_message(userid, dialog, dialog).title
            result.append(
                viewo_helpdesk.Dialog(
                    userid=userid,
                    date=dialog,
                    title=title,
                ))
    return result


def load_users() -> list:
    board = viewo_helpdesk.board()
    users = utilo.file_list(board)
    return users


def valid_user(userid: str) -> bool:
    board = viewo_helpdesk.board()
    userpath = os.path.join(board, userid)
    if not os.path.exists(userpath):
        return False
    return True


def valid_dialog(userid: str, date: int) -> bool:
    if not valid_user(userid):
        return False
    date = f'{date}'
    board = viewo_helpdesk.board()
    dialogpath = os.path.join(board, userid, date)
    if not os.path.exists(dialogpath):
        return False
    return True


def load_after(date: int, userid: int = None):  # pylint:disable=W0613
    pass


def load_before(data: int, userid: int = None):  # pylint:disable=W0613
    pass
