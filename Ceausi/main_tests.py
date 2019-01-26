# -*- coding: utf-8 -*-

import sys

from lib import *
from tests import *

if __name__ == '__main__':
    t = Tests(sys.argv[1])
    t.run_test()
