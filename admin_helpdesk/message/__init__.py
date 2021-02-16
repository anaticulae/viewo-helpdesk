# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class Message:
    parent: int = None
    userid: str = None
    date: int = None
    title: str = None
    text: str = None
    writer: str = None
    category: int = None


Messages = typing.List[Message]


@dataclasses.dataclass
class Dialog:
    userid: str = None
    date: int = None
    title: str = None


Dialogs = typing.List[Dialog]
