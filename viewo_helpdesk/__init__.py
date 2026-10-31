#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import importlib.metadata
import os

import utilo

import viewo_helpdesk.__patch__
from viewo_helpdesk.api import api_call
from viewo_helpdesk.config import API_PREFIX
from viewo_helpdesk.config import SECRET_KEY
from viewo_helpdesk.config import VIEWO_HELPDESK
from viewo_helpdesk.config import board
from viewo_helpdesk.config import configure
from viewo_helpdesk.message import Dialog
from viewo_helpdesk.message import Dialogs
from viewo_helpdesk.message import Message
from viewo_helpdesk.message import Messages
from viewo_helpdesk.message.action import start_conversion
from viewo_helpdesk.message.action import write_message
from viewo_helpdesk.message.collect import load_dialogs
from viewo_helpdesk.message.collect import load_messages
from viewo_helpdesk.message.collect import load_users
from viewo_helpdesk.message.collect import valid_dialog
from viewo_helpdesk.message.collect import valid_user
from viewo_helpdesk.message.path import userpath
from viewo_helpdesk.message.serialize import dump_message

__version__ = importlib.metadata.version('viewo-helpdesk')

ROOT = os.path.abspath(utilo.join(os.path.dirname(__file__), '..'))
