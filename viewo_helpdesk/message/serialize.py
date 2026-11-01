# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import viewo_helpdesk.message


def dump_message(message: viewo_helpdesk.message.Message) -> str:
    raw = f'{message.title}\n\n{message.text}'
    return raw
