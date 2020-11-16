#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

from admin_helpdesk.app import now
from admin_helpdesk.config import board
from admin_helpdesk.fixtures import appi
from admin_helpdesk.fixtures import client
from admin_helpdesk.message import Message
from admin_helpdesk.message import Messages
from admin_helpdesk.message.action import start_conversion
from admin_helpdesk.message.action import write_message
from admin_helpdesk.message.collect import load_messages
from admin_helpdesk.message.collect import load_users
from admin_helpdesk.message.path import userpath
from admin_helpdesk.message.serialize import dump_message

__version__ = '0.0.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
