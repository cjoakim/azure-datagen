__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.05.28"

import pytest

from pysrc.cjcc.constants import Constants


def test_kilobyte():
    assert(Constants.kilobyte() == 1024)
