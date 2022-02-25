__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "2020.10.22"

import pytest

from pysrc.cjcc.bytes import Bytes 


def test_human_readable():
    assert(Bytes.human_readable(100) == '100')
    assert(Bytes.human_readable(1000.4) == '1,000.4')
    assert(Bytes.human_readable(123456789.5) == '123,456,789.5')
    assert(Bytes.human_readable(100000000000002) == '100,000,000,000,002')

    b = Bytes.terabytes(17)  # 18691697672192
    assert(Bytes.human_readable(b) == '18,691,697,672,192.0')

    gb = Bytes.as_gigabytes(b)  # 17408.0
    print(gb)
    assert(Bytes.human_readable(gb) == '17,408.0')

def test_kilobyte():
    assert(Bytes.kilobyte() == 1024)

def test_kilobytes():
    assert(Bytes.kilobytes(2) == 2048)

def test_megabyte():
    assert(Bytes.megabyte() == 1048576)

def test_megabytes():
    assert(Bytes.megabytes(2) == 2097152)

def test_gigabyte():
    assert(Bytes.gigabyte() == 1073741824)

def test_gigabytes():
    assert(Bytes.gigabytes(2) == 2147483648)

def test_terabyte():
    assert(Bytes.terabyte() == 1099511627776)

def test_terabytes():
    assert(Bytes.terabytes(2) == 2199023255552)

def test_petabyte():
    assert(Bytes.petabyte() == 1125899906842624)

def test_petabytes():
    assert(Bytes.petabytes(2) == 2251799813685248)

def test_exabyte():
    assert(Bytes.exabyte() == 1152921504606846976)

def test_exabytes():
    assert(Bytes.exabytes(2) == 2305843009213693952)

def test_zettabyte():
    assert(Bytes.zettabyte() == 1180591620717411303424)

def test_zettabytes():
    assert(Bytes.zettabytes(2) == 2361183241434822606848)

def test_yottabyte():
    assert(Bytes.yottabyte() == 1208925819614629174706176)

def test_yottabytes():
    assert(Bytes.yottabytes(2) == 2417851639229258349412352)

def test_as_kilobytes():
    assert(Bytes.as_kilobytes(0) == -.0)
    assert(Bytes.as_kilobytes(1024) == 1.0)
    assert(Bytes.as_kilobytes(4096) == 4.0)
    assert(Bytes.as_kilobytes(10000) == 9.765625)

def test_as_megabytes():
    assert(Bytes.as_megabytes(0) == 0.0)
    assert(Bytes.as_megabytes(1048576) == 1.0)
    assert(Bytes.as_megabytes(13631488) == 13.0)
    assert(Bytes.as_megabytes(20000000) == 19.073486328125)

def test_as_gigabytes():
    assert(Bytes.as_gigabytes(0) == 0.0)
    assert(Bytes.as_gigabytes(1073741824) == 1.0)
    assert(Bytes.as_gigabytes(8589934592) == 8.0)
    assert(Bytes.as_gigabytes(1048576) == 0.0009765625)


