"""
Usage:
  python main.py <func>
  python main.py create_module Thing
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "February 2022"

# from datetime import date, datetime, timedelta
# from dateutil import tz

import json
import sys
import time
import os

import arrow 

from docopt import docopt

from pysrc.env import Env
from pysrc.excel import Excel
from pysrc.fs import FS
from pysrc.template import Template


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)

def check_env():
    print("==========\ncheck_env:")
    home = Env.var('HOME')
    print('home: {}'.format(home))


if __name__ == "__main__":

    # dispatch to a main function based either on the first command-line arg,
    # or on the MAIN_PY_FUNCTION environment variable when run as a container.

    func = sys.argv[1].lower()

    if func == 'env':
        check_env()
    else:
        print_options('Error: invalid function: {}'.format(func))
