__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.05.28"

import pytest

from pysrc.cjcc.eventhub import EventHub
from pysrc.cjcc.env import Env

# TODO: Implement tests

def test_constructor():
    opts = dict()
    opts['conn_str'] = Env.var('AZURE_EVENTHUB_CONN_STRING')
    opts['hub_name'] = Env.var('AZURE_EVENTHUB_HUBNAME')
    opts['verbose']  = False
    eh = EventHub(opts)

    assert(eh.mode() == 'producer')
    assert(eh.is_consumer() == False)
    assert(eh.verbose() == False)
    assert(eh.state() == 'open')

    eh.close()
    assert(eh.state() == 'closed')
