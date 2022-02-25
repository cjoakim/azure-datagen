__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.10.11"

import pytest

from pysrc.cjcc.env import Env


def test_var():
    assert(Env.var('SHELL') == '/bin/bash')
    assert(Env.var('USER') == 'cjoakim')
    assert(Env.var('MISSING', '42') == '42')

def test_epoch():
    e1 = Env.epoch()
    assert(e1 > 1587667642)
    assert(e1 < 1650000000)
    Env.sleep(1)
    e2 = Env.epoch()
    assert(e2 > e1)
    assert(e2 < (e1 + 2))
