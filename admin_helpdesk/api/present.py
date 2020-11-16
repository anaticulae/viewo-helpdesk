# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import admin_helpdesk
import admin_helpdesk.api
import admin_helpdesk.api.auth


@admin_helpdesk.api.api_message.route(
    '/dialogs',
    methods=['GET'],
    defaults={'userid': None},
)
@admin_helpdesk.api.auth.admin_required
def dialogs(userid: str):
    result = admin_helpdesk.load_dialogs(userid)
    dumped = admin_helpdesk.api.dump(result, 'dialogs')
    return dumped


@admin_helpdesk.api.api_message.route(
    '/dialog/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
def dialog_get(userid: str, date: int):
    messages = admin_helpdesk.load_messages(userid, date)
    dumped = admin_helpdesk.api.dump(messages, 'messages')
    return dumped
