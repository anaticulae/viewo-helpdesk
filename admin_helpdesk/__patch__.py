# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum
import os

import utila


def directory_list(path: str) -> list:
    assert os.path.exists(path), path
    result = []
    for item in os.scandir(path):
        if not item.is_dir():
            continue
        result.append(item.name)
    return result


utila.directory_list = directory_list


def simplify(item):
    if isinstance(item, enum.Enum):
        return item.value
    if isinstance(item, list):
        return [simplify(it) for it in item]
    if isinstance(item, tuple):
        return tuple([simplify(it) for it in item])
    try:
        item = vars(item)
    except TypeError:
        return item
    for key, value in item.items():
        item[key] = simplify(value)
    return item


utila.simplify = simplify
