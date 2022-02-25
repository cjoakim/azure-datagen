__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.05.28"

import pytest

from pysrc.cjcc.fs import FS
from pysrc.cjcc.template import Template


def test_template_lookup_and_rendering():
    values = dict()
    values['group'] = 'Dire Straits'
    values['artist'] = 'Mark Knopfler'
    t = Template.get_template(FS.pwd(), 'unit_tested.txt')
    code = Template.render(t, values)
    lines = code.split("\n")
    assert(len(lines) == 4)
    assert(lines[0] == 'Header line')
    assert(lines[1] == 'Group: Dire Straits')
    assert(lines[2] == 'Artist: Mark Knopfler')
    assert(lines[3] == 'Last line')