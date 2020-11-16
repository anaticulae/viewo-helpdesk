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


@admin_helpdesk.api.api_message.route('/dialogs', methods=['GET'])
@admin_helpdesk.api.auth.admin_required
def dialogs():
    result = admin_helpdesk.load_dialogs()
    dumped = admin_helpdesk.api.dump(result, 'dialogs')
    return dumped


@admin_helpdesk.api.api_message.route(
    '/dialogs/<string(length=16):userid>',
    methods=['GET'],
)
def dialogs_get(userid: str):
    return ''


@admin_helpdesk.api.api_message.route(
    '/dialogs/<string(length=16):userid>/<int:date>',
    methods=['GET'],
)
def dialog_get(userid: str, date: int):
    return ''
