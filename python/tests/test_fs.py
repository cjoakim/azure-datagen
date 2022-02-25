__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.05.28"

import pytest
import datetime
import json

from pysrc.cjcc.fs import FS


def test_pwd():
    s = FS.pwd()
    assert(s == "/Users/cjoakim/github/cj-py")

def test_read():
    s = FS.read('data/u2.txt')
    assert(len(s) == 43)
    assert(s == "bono\nthe edge\nadam clayton\nlarry mullen jr\n")

    s = FS.read('data/nc_zipcodes.json')
    assert(len(s) == 304618)

def test_read_lines():
    lines = FS.read_lines('data/postal_codes_nc.csv')
    assert(len(lines) == 1081)
    assert(lines[0] == "id,postal_cd,country_cd,city_name,state_abbrv,latitude,longitude\n")
    assert(lines[-1] == "12028,28909,US,Warne,NC,35.0118070000,-83.9188180000\n")

def test_read_json():
    obj = FS.read_json('data/nc_zipcodes.json')
    #print(obj)
    assert(str(type(obj)) == "<class 'list'>")
    assert(len(obj) == 1075)

def test_read_csv_with_header():
    rows = FS.read_csv('data/postal_codes_nc.csv')
    assert(len(rows) == 1081)
    print(rows[0])
    print(rows[-1])
    assert(rows[0] == ['id', 'postal_cd', 'country_cd', 'city_name', 'state_abbrv', 'latitude', 'longitude'])
    assert(rows[-1] == ['12028', '28909', 'US', 'Warne', 'NC', '35.0118070000', '-83.9188180000'])

def test_read_csv_skip_header():
    rows = FS.read_csv('data/postal_codes_nc.csv', skip=1)
    assert(len(rows) == 1080)
    print(rows[0])
    print(rows[-1])
    assert(rows[0] == ['10949', '27006', 'US', 'Advance', 'NC', '35.9445620000', '-80.4376310000'])
    assert(rows[-1] == ['12028', '28909', 'US', 'Warne', 'NC', '35.0118070000', '-83.9188180000'])

def test_read_csv_dict_reader():
    rows = FS.read_csv('data/postal_codes_nc.csv', reader='dict')
    assert(len(rows) == 1080)
    assert(rows[0]['postal_cd'] == '27006')
    assert(rows[-1]['postal_cd'] == '28909')

def test_text_file_iterator():
    it = FS.text_file_iterator('data/postal_codes_nc.csv')
    first_line, curr_line, count = None, None, 0
    for i, line in enumerate(it):
        count = count + 1
        if i == 0:
            first_line = line
        curr_line = line
    assert(first_line == 'id,postal_cd,country_cd,city_name,state_abbrv,latitude,longitude')
    assert(curr_line == '12028,28909,US,Warne,NC,35.0118070000,-83.9188180000')
    assert(count == 1081)

def test_write():
    testfile = 'tmp/test_write.txt'
    s1 = "line 1\nline2\ncreated at {}".format(datetime.datetime.now())
    FS.write(testfile, s1)
    s2 = FS.read(testfile)
    assert(s1 == s2)

def test_walk():
    entries = FS.walk('data')
    print(json.dumps(entries, sort_keys=True, indent=2))
    assert(len(entries) > 7)
    assert(len(entries) < 13)
    mk_found = False
    for e in entries:
        if e['base'] == 'mark_knophler.txt':
            mk_found = True
            assert(e['dir'] == 'data/artists')
            assert(e['full'] == 'data/artists/mark_knophler.txt')
            assert(e['abspath'] == '/Users/cjoakim/github/cj-py/data/artists/mark_knophler.txt')
    assert(mk_found)
